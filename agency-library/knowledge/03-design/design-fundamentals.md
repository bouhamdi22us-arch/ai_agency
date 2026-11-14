# Fundamentos de diseño

> **Departamento:** 03 · **Tipo:** fundamentos · **Última revisión:** 2026-11-14 · **Estado:** establecido

## Qué es / Para qué
Principios que previenen el 80% de fallos visuales y de producto sin depender del gusto.

## Core concepts
- **Jerarquía** — el tamaño, peso, contraste y espaciamiento comunican orden; si todo destaca, nada destaca.
- **Grid & espaciado** — escala tipográfica (ratio ~1.2–1.333) y múltiplo de 4/8 px; márgenes consistentes.
- **Color** — 1 neutro dominante + 1 acento + semánticos (éxito/aviso/error); contraste WCAG ≥ 4.5:1 texto normal, ≥ 3:1 grande.
- **Sistema** — tokens (color, tipografía, espaciado, radios) + componentes documentados; cualquier cambio se propaga sin rehacer páginas.
- **Accesibilidad** — no es un plus: teclado, contraste, foco visible, alternativas textuales, reduced-motion.

## Principios
1. Función antes que ornamento; la estética reporta a la claridad.
2. Contraste y agrupación son los dos mecanismos cognitivos básicos.
3. La tipografía es el 90% del diseño gráfico: elige pocas, buen pairing (sans + serif de carácter).
4. Menos elementos, mejores elementos — la poda mejora el diseño.
5. Prueba la interfaz en móvil real y al 200% de zoom.

## Procedimiento
1. Intentado: define objetivo de la pantalla en una frase (sin anécdota de marca).
2. Inventario de elementos → prioriza por orden de lectura esperado.
3. Estructura: jerarquía (tamaño/peso), alineación en grid, espaciado base-8.
4. Revisa foco visible y orden de tabulación (teclado solo).
5. Revisa contraste con herramienta (p.ej. cálculo por luminancia); ajusta acentos.
6. Documenta tokens; no valores sueltos en CSS.

## Errores comunes
- Gradientes y sombras decorativas que compiten con el contenido.
- Texto gris claro sobre blanco como "elegante" — ilegible e inaccesible.
- PLACEHOLDER sin labels; foco invisible;
- Layout que colapsa con texto real ("el cliente lo escribirá corto" — no lo hará).
- Rediseñar una pantalla sin sistema: el problema vuelve en la siguiente.

## Más lectura
- NN/g articles — https://www.nngroup.com/articles/ — 2026-11-14
- WCAG 2.2 — https://www.w3.org/WAI/standards-guidelines/wcag/ — 2026-11-14
- refactoringui.com (técnicas prácticas) — buscar en el índice
- The Design of Everyday Things — libros.md

## Fuentes
NNG/WCAG verificados; recomendación de sistema basada en práctica (marcada como tal).
