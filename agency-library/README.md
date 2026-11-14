# Agency Knowledge Library

Biblioteca de conocimiento profesional de **la agencia** (agents: ATLAS, AGENTS ORCHESTRATOR,
y todos los líderes departamentales). No es una carpeta de notas: es un sistema de conocimiento
organizado, basado en evidencia y mantenido.

## Qué hay aquí

| Capa | Contenido |
|---|---|
| `knowledge/<nn-departamento>/` | Conocimiento propio (educativo, en palabras propias): definiciones, frameworks, procedimientos, errores comunes. **Teoría y ejecución práctica separadas por documento.** |
| `knowledge/<nn>/README.md` | Índice del departamento: mapa de temas, recursos clave, cuándo consultar. |
| `catalog/` | Recursos externos verificados (`resources.md`), frameworks (`frameworks.md`), libros (`books.md`). Metadatos completos; URLs comprobadas el 2026-11-14 cuando se indica. |
| `GLOSSARY.md` | Vocabulario común de la agencia. |
| `cross-references.md` | "Si buscas X → ve a Y". |
| `MAINTENANCE.md` | Cómo mantener y ampliar la biblioteca. |
| `templates/` | Plantilla de documento de conocimiento. |

## Navegación

Empieza por `INDEX.md`. Cada departamento tiene su README con su mapa de temas y sus 5-8 recursos principales.
Búsqueda rápida: `grep -ri "término" agency-library`.

## Principios de la biblioteca

1. **La evidencia manda.** Cada documento indica qué es conocimiento establecido y qué es interpretación/recomendación.
2. **Fuentes mejor que opiniones.** Canon sobre efímero: documentación oficial y textos primarios antes que resúmenes.
3. **Nada inventado.** Recursos, enlaces, autores y fechas están verificados o marcados como *no verificados*.
4. **No se copian obras protegidas.** Se guardan referencias y resúmenes propios.
5. **Vivo.** Toda contribución pasa por `MAINTENANCE.md`.

## Cómo la usan los agentes

- Antes de inventar doctrina, un agente busca aquí (`grep`/lectura de índices).
- Al entregar conocimiento nuevo a un cliente/PRD/estrategia, cita la fuente.
- Si falta un tema: se añade siguiendo la plantilla (ver `MAINTENANCE.md`) y se actualiza el índice.

_Ubicación: `agency-library/` · Creada: 2026-11-14 · Alcance local (no desplegada)._
