# Mantenimiento de la biblioteca

## Cuándo actualizar

- Tras cada proyecto con aprendizaje nuevo (agente o humano).
- Trimestralmente: revisión de recursos externos (¿siguen vivos? ¿siguen siendo buenos?).
- Ante descubrimiento de una fuente Tier 1 que contradiga un documento: se corrige el documento y se anota el cambio.

## Cómo añadir/cambiar un documento

1. Parte de `templates/knowledge-doc-template.md`.
2. Escribe en palabras propias; cita fuentes con URL y fecha.
3. Marca lo que es **establecido** (canon) y lo que es **interpretación** (tu criterio).
4. Añade el documento al índice del departamento y a `INDEX.md` si crea sección nueva.
5. Si hay recursos nuevos, actualiza `catalog/resources.md` (con fecha de verificación).
6. Commits semánticos: `docs(library): add …`.

## Estándar de calidad (checklist de aceptación)

- [ ] Propósito claro y audiencia definida
- [ ] Definiciones y conceptos antes que frameworks
- [ ] Fuentes citadas, con fecha
- [ ] Sección "Errores comunes"
- [ ] Sección "Más lectura"
- [ ] Sin afirmaciones factuales sin fuente; sin números inventados
- [ ] Nada de copiar obras protegidas completa (solo referencias + resúmenes propios)
- [ ] Índices actualizados

## Poda y salud

- Documento que no aporta sobre los existentes → se fusiona o se borra (con commit explicativo).
- Enlaces muertos → marcar `[ENLACE ROTO]` o sustituir por sucesor oficial.
- Duplicación → una fuente de verdad; el resto enlaza a ella.
