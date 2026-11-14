# Agency Operating System (AOS)

> Protocolo único de funcionamiento de la agencia. Aplica a TODOS los agentes por igual.
> Regla madre: **un agente solo opera tan bien como la misión que recibe** — por eso cada asignación lleva TODO el contexto, y cada entrega pasa por un gate antes de aceptarse.

## Fase actual: COMPLETA (doctrina + CLI)

Fase 1 = doctrina (abajo). Fase 2 = `aos`, un CLI sin dependencias (Python 3 stdlib):
`agency-library/aos/aos.py` (enlazado a `/usr/local/bin/aos`). Almacén: `~/.config/opencode/aos/queue.json`.

```
aos init                      crea el almacén
aos add <proyecto> <agente> <título>   nueva tarea (pending)
aos list [--project P|--agent A|--status S]
aos start <id> [--agent A]    reclama (pending → in_progress, anti doble-claim)
aos done <id> --note "evidencia"   cierra (nota obligatoria)
aos cancel <id> --reason "..."        cancela (no cierra algo done)
aos status                    resumen por agente y proyecto
aos brief <id>                brief de asignación rellenado
```

Verificado en sesión: barreras anti doble-claim y cierre sin nota funcionan; done sin start se registra a propósito; estado agrega bien por agente/proyecto.

## Limitaciones honestas
- Estado local-filesystem, sin sincronización entre agentes simultáneos sobre la misma cola (race conditions posibles) ni locks.
- No es enforcement del modelo: los agentes pueden ignorarlo; los gates de `03` son disciplina, no garantía técnica.
- No cubre memoria semántica de proyectos (usa `05-ledger.md` para eso).

| Documento | Para qué |
|---|---|
| `01-operating-protocol.md` | El ciclo exacto de cada objetivo: FRAME → BRIEF → PLAN → DISPATCH → VERIFY → CLOSE |
| `02-anti-confusion-rules.md` | Las reglas anti-"liarse": límites, bucles, saturación de contexto, verificación obligatoria |
| `03-quality-gates.md` | Puertas de calidad por tipo de entrega (código, copy, diseño, research, plan) |
| `04-brief-template.md` | Plantilla de asignación — cada miembro recibe esto, o la tarea no empieza |
| `05-ledger.md` | Memoria entre sesiones: PROGRESS.md/DECISIONS.md por proyecto |
| `06-handoff-protocol.md` | Cómo se pasa trabajo entre agentes y al founder |
| `07-escalation-matrix.md` | Quién decide qué; qué nunca se puede hacer sin autorización |

Fase 2 (mini-software): `aos`, una CLI local con cola y estados de tareas sobre la misma doctrina.
