# 05 · Ledger — memoria del proyecto entre sesiones

Cada proyecto relevante mantiene en su raíz (o en la del repositorio):

```
<project>/
  PROGRESS.md     — estado actual: hecho / en curso / bloqueado / siguiente
  DECISIONS.md    — decisiones + fecha + razón (una línea c/u)
  OPEN-QUESTIONS.md — dudas sin resolver
```

## Formato PROGRESS.md
```
# PROGRESS — <project>
_Última actualización: YYYY-MM-DD_
## Hecho
- <bullet> (commit/hash si aplica)
## En curso
- <bullet> — dueño: <agente>
## Bloqueado
- <bullet> — esperando: <quién/qué>
## Siguiente
- <bullet>
```

## DECISIONS.md
- `YYYY-MM-DD — Elegimos X porque Y (rechazado: Z).`
- Una línea por decisión; si es grande, enlaza al doc completo.

## Regla
- Todo agente que entrega actualiza PROGRESS.md en la misma entrega.
- Nuevas sesiones: leer PROGRESS + DECISIONS antes de tocar nada.
- Ledger del OpenCode execution (subagent-driven-development) vive aparte: `.superpowers/sdd/<plan>/`.
