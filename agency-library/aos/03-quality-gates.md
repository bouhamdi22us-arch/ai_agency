# 03 · Quality gates por tipo de entrega

Cada entrega pasa por **su** gate. El que entrega ejecuta el gate ANTES de decir "listo". Entrega crítica (dinero, prod, legal, marca): gate independiente además.

## Code (MARCO/NOVA)
- [ ] Tests existen y estaban rojos antes del fix (bug) o cubren el comportamiento (feature)
- [ ] Suite entera verde; `node --check`/build ok
- [ ] Sin dependencias nuevas innecesarias; sin secretos; migraciones reversibles
- [ ] Foco visible, reduced-motion, responsive 360px (UI)
- [ ] Docs/ADR solo si hay decisión estructural

## Design (SOFIA)
- [ ] Concept claro y justificado frente al brief
- [ ] Clase de marca/commodity verificada (nada genérico sin razón)
- [ ] Sistema (tokens) o medidas exactas; sin placeholders
- [ ] A11y: contraste medido, foco visible, teclado completo
- [ ] Review con datos worst-case (break de edge cases)

## Copy/Ads/Contenido (JACK)
- [ ] Claims verificables o marcados como hipótesis
- [ ] CTA único; lenguaje del cliente; sin AI-tells
- [ ] ICP/posicionamiento coherente (product-marketing doc si existe)
- [ ] Métrica de éxito declarada si es campaña

## Research/Intelligence (VICTORIA)
- [ ] Tier 1/2/3 citas para cada claim importante
- [ ] Distinción hecho vs interpretación explicitada
- [ ] Confianza global declarada + limitaciones
- [ ] 16-20 palabras mín. de contexto por recomendación

## Estrategia/Plan (ATLAS/FOSTER/OLIVIA)
- [ ] Diagnóstico + opción recomendada + razones + rechazados
- [ ] Iniciativas numeradas con responsable, deadline, criterio de éxito
- [ ] Riesgos y supuestos explícitos, no ocultos

## Cierre (todos)
- [ ] El entregable existe en disco/enlace (no en la cabeza)
- [ ] Nada "al 90%" se declara listo
