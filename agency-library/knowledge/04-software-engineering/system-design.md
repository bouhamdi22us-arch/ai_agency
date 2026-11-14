# System design — enfoque y trade-offs

> **Departamento:** 04 · **Tipo:** fundamentos · **Última revisión:** 2026-11-14 · **Estado:** establecido

## Qué es / Para qué
Método para decidir arquitectura de software controlando la complejidad y explicitando trade-offs.

## Core concepts
- **Trade-off fundamental** — cada decisión sacrifica simplicidad, coste, latencia, consistencia o velocidad.
- **CAP / PACELC** — en partición: consistencia vs. disponibilidad; sin partición: latencia vs. consistencia.
- **ACID vs. BASE** — integridad estricta vs. disponibilidad y escala.
- **Escalado vertical → horizontal** — empezar monolítico con límites claros; extraer servicios cuando hay cuello de botella medido (no por moda).
- **Diseño para operación** — logs estructurados, métricas RED (rate/errors/duration), timeouts y retries con backoff.

## Marco de análisis
1. **Requisitos** — funcionales + no funcionales (tráfico, latencia SLO, consistencia, retención de datos).
2. **API first** — contratos antes de implementación (REST/gRPC/eventos).
3. **Datos** — modelo de datos, cardinalidad, índices, migraciones; la base de datos decide más que el framework.
4. **Lectura/escritura** — cache (read-through), colas para desacople, idempotencia.
5. **Fallos** — qué pasa si esto cae: retries, circuit breaker, degradación elegante.

## Errores comunes
- Microservicios para un equipo de 3 y un producto sin usuarios.
- Dependencias por moda; cada una es superficie de ataque y mantenimiento.
- Optimizar antes de medir (perfilar primero: el cuello casi nunca es el que crees).
- Sin migraciones reversibles; sin backups probados (un backup sin restore-test = no existe).
- Confiar en variables de entorno sueltas para secretos en vez de un gestor.

## Más lectura
- Designing Data-Intensive Applications — Martin Kleppmann — libros.md
- Kubernetes docs — https://kubernetes.io/docs — 2026-11-14
- OWASP Top 10 — https://owasp.org — buscar en catálogo
- PostgreSQL docs — https://www.postgresql.org/docs/current/ — 2026-11-14

## Fuentes
Docs oficiales verificados 2026-11-14; teoría de Kleppmann (referenciada, no reproducida).
