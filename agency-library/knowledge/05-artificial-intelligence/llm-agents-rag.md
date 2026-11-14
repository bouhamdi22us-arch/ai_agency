# LLMs, agentes y RAG — de texto a sistema fiable

> **Departamento:** 05 · **Tipo:** fundamentos · **Última revisión:** 2026-11-14 · **Estado:** establecido

## Qué es / Para qué
Convertir un modelo probabilístico en un sistema que hace trabajo útil con presupuesto y riesgo conocidos.

## Core concepts
- **Contexto** — todo lo que el modelo ve; tokens caros; menos y más preciso > más.
- **Grounding** — el modelo compone texto; verdad viene de fuentes provistas (RAG, herramientas) — no se sabe de memoria.
- **Structured outputs / function calling** — contratos JSON con esquemas; validar siempre con parsing, nunca confiar.
- **Agent** — LLM + herramientas + bucle de decisión; no es "un chatbot". Ventaja solo con objetivos y límites.
- **RAG** — recuperación antes de generación: chunking → embeddings → búsqueda (+ rerank) → generación con citas.
- **Evaluación** — medir éxito (tareas completadas, precisión, coste/tarea), no "qué tal suena".

## Principios prácticos
1. Prompting simple → structured outputs → herramientas → RAG → fine-tune: escala por orden, solo si el anterior no basta.
2. Humano-en-el-loop para irreversible o sensible; autonomía para barato y reversible.
3. Coste = tokens × precio; mide tokens/tarea en producción.
4. Guardrails en salidas (filtros, validación de esquema) antes de efectos externos.
5. Versionar prompts como código.

## Procedimiento (decisión de arquitectura)
1. Define la tarea en criterios verificables (qué cuenta como hecho).
2. Intenta baseline simple; mide contra 20–50 casos representativos.
3. Si falta conocimiento propietario → RAG; si falta interacción con el mundo → herramientas/agente; si falta estilo/formato → prompting/SFT.
4. Añade evals y alarmas (regresión de calidad) antes de escalar.

## Errores comunes
- "Poner un chatbot" sin definir la tarea y el criterio de éxito.
- RAG sin citas: imposible auditar respuestas.
- Agente sin presupuesto de pasos/coste: bucles caros y errores en cadena.
- Fine-tuning antes de agotar prompting; datos malos amplificados.
- Confiar salidas sin validación en pagos, correos o borrados.

## Más lectura
- Hugging Face docs — https://huggingface.co — 2026-11-14
- arXiv (cs.CL, cs.IR) — https://arxiv.org — 2026-11-14
- Designing Machine Learning Systems — books.md

## Fuentes
Docs verificadas; frameworks conceptuales consolidados (paper-first), aquí en palabras propias.
