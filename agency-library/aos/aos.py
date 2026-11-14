#!/usr/bin/env python3
"""aos — Agency Operating System: cola y estado de tareas de la agencia.

Implementa la doctrina de agency-library/aos/ en una herramienta local
sin dependencias. Almacén de estado: ~/.config/opencode/aos/queue.json

Comandos:
  aos init                                   crea el almacén
  aos add <proyecto> <agente> <titulo>...    crea una tarea (pending)
  aos list [--project P] [--agent A]          lista tareas
         [--status pending|in_progress|done|cancelled]
  aos start <id> [--agent A]                  reclama la tarea (pending → in_progress)
  aos done <id> --note "..."                  cierra la tarea (exige evidencia/nota)
  aos cancel <id> --reason "..."              cancela la tarea
  aos status                                   resumen por agente y proyecto
  aos brief <id>                               emite el brief de asignación rellenado
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

STORE = Path.home() / ".config" / "opencode" / "aos" / "queue.json"


def load():
    if not STORE.exists():
        die("no hay almacén: ejecuta `aos init`")
    return json.loads(STORE.read_text())


def save(tasks):
    STORE.parent.mkdir(parents=True, exist_ok=True)
    STORE.write_text(json.dumps(tasks, ensure_ascii=False, indent=2))


def die(msg):
    print(f"aos: {msg}", file=sys.stderr)
    sys.exit(1)


def new_id(tasks):
    return (max([t["id"] for t in tasks], default=0)) + 1


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def find(tasks, tid):
    for t in tasks:
        if t["id"] == tid:
            return t
    die(f"tarea {tid} no existe")


def cmd_init(_):
    if STORE.exists():
        die(f"ya existe {STORE} (no se sobrescribe)")
    save([])
    print(f"OK — almacén creado en {STORE}")


def cmd_add(args):
    tasks = load()
    tid = new_id(tasks)
    tasks.append({
        "id": tid,
        "project": args.project.lower(),
        "agent": args.agent.lower(),
        "title": " ".join(args.title),
        "status": "pending",
        "created_at": now(),
        "started_at": None,
        "done_at": None,
        "note": None,
        "cancel_reason": None,
    })
    save(tasks)
    print(f"tarea {tid} creada (pending) → [{args.project}] {' '.join(args.title)} → {args.agent}")


def cmd_list(args):
    tasks = load()
    for t in tasks:
        if args.project and t["project"] != args.project.lower():
            continue
        if args.agent and t["agent"] != args.agent.lower():
            continue
        if args.status and t["status"] != args.status:
            continue
        mark = {"pending": "·", "in_progress": "▸", "done": "✓", "cancelled": "✗"}[t["status"]]
        print(f"{mark} {t['id']:>3} [{t['project']}] ({t['agent']}) {t['title']}"
              + (f" — {t['note']}" if t["note"] else ""))


def cmd_start(args):
    tasks = load()
    t = find(tasks, args.id)
    if t["status"] != "pending":
        die(f"la tarea {t['id']} está '{t['status']}', solo se reclaman 'pending'")
    t["status"] = "in_progress"
    t["started_at"] = now()
    t["started_by"] = args.agent or t["agent"]
    save(tasks)
    print(f"tarea {t['id']} → in_progress ({t['started_by']}) — {t['title']}")


def cmd_done(args):
    if not args.note.strip():
        die("--note obligatorio: qué evidencia/decisión cierra la tarea")
    tasks = load()
    t = find(tasks, args.id)
    if t["status"] not in ("in_progress", "pending"):
        die(f"la tarea {t['id']} está '{t['status']}', no se puede cerrar")
    t["status"] = "done"
    t["done_at"] = now()
    t["note"] = args.note
    save(tasks)
    print(f"tarea {t['id']} → done — {t['note']}")


def cmd_cancel(args):
    if not args.reason.strip():
        die("--reason obligatorio")
    tasks = load()
    t = find(tasks, args.id)
    if t["status"] == "done":
        die(f"la tarea {t['id']} ya está done; no se cancela")
    t["status"] = "cancelled"
    t["cancel_reason"] = args.reason
    save(tasks)
    print(f"tarea {t['id']} → cancelled — {t['cancel_reason']}")


def cmd_status(_):
    tasks = load()
    agg, by_project = {}, {}
    for t in tasks:
        agg.setdefault(t["agent"], {}).setdefault(t["status"], 0)
        agg[t["agent"]][t["status"]] += 1
        by_project.setdefault(t["project"], {}).setdefault(t["status"], 0)
        by_project[t["project"]][t["status"]] += 1
    def block(name, data):
        print(name)
        if not data:
            print("  (vacío)")
        for key in sorted(data):
            s = data[key]
            statuses = " · ".join(f"{k}:{v}" for k, v in sorted(s.items()))
            print(f"  {key:<24} {statuses}")
    block("STATUS por agente", agg)
    block("STATUS por proyecto", by_project)


def cmd_brief(args):
    tasks = load()
    t = find(tasks, args.id)
    print(f"""## TASK ASSIGNMENT

**Project:**        {t['project']}
**Assigned to:**    {t['agent']}
**Objective:**      {t['title']}
**Deliverable:**    [archivo/ruta esperado]
**Acceptance:**     [criteria verificables — rellenar antes de enviar]
**Constraints:**    [presupuesto, tiempo, stack, marca]
**Dependencies:**   [lista]
**Quality level:**  NORMAL
""")


def main():
    p = argparse.ArgumentParser(prog="aos", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init", help="crea el almacén").set_defaults(func=cmd_init)

    ap = sub.add_parser("add", help="crea tarea")
    ap.add_argument("project")
    ap.add_argument("agent")
    ap.add_argument("title", nargs="+")
    ap.set_defaults(func=cmd_add)

    ap = sub.add_parser("list", help="lista tareas")
    ap.add_argument("--project")
    ap.add_argument("--agent")
    ap.add_argument("--status", choices=["pending", "in_progress", "done", "cancelled"])
    ap.set_defaults(func=cmd_list)

    ap = sub.add_parser("start", help="reclama tarea")
    ap.add_argument("id", type=int)
    ap.add_argument("--agent")
    ap.set_defaults(func=cmd_start)

    ap = sub.add_parser("done", help="cierra tarea (nota obligatoria)")
    ap.add_argument("id", type=int)
    ap.add_argument("--note", required=True)
    ap.set_defaults(func=cmd_done)

    ap = sub.add_parser("cancel", help="cancela tarea")
    ap.add_argument("id", type=int)
    ap.add_argument("--reason", required=True)
    ap.set_defaults(func=cmd_cancel)

    sub.add_parser("status", help="resumen").set_defaults(func=cmd_status)

    ap = sub.add_parser("brief", help="brief rellenado")
    ap.add_argument("id", type=int)
    ap.set_defaults(func=cmd_brief)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
