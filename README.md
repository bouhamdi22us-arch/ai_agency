# AI Agency — OpenCode Agency OS

Sistema completo de una **agencia de IA** construido sobre [OpenCode](https://opencode.ai):
agentes ejecutivos y departamentales, biblioteca de conocimiento propia (Agency Knowledge Library),
Agency Operating System (AOS) y la colección de skills instaladas.

Todo ello publicado como **open source** para que cualquiera pueda usarlo, estudiarlo o adaptarlo.

## ¿Qué hay aquí?

| Carpeta | Contenido | Autoría |
|---|---|---|
| `agents/` | 11 agentes: ATLAS (CEO), agentes departamentales (growth, producto, ingeniería, diseño, investigación, operaciones, ventas, marketing, IA, orquestador) | Propio (MIT) |
| `agency-library/` | Biblioteca de conocimiento: 11 departamentos, catálogos verificados, glosario, referencias cruzadas y **AOS** (`agency-library/aos/`): protocolo operativo, reglas anti-confusión, quality gates, plantillas de brief, ledger, handoff, escalado y CLI `aos` | Propio (MIT) |
| `skills/` | 175 skills para agentes (marketing, ingeniería, diseño, producto, investigación…). **Skills de terceros**, copiadas sin modificar, cada una bajo su licencia | Terceros — ver [CREDITS.md](CREDITS.md) |

## Estructura

```
agents/            → copia en ~/.config/opencode/agents/
agency-library/    → copia en ~/agency-library/ (o ajusta las rutas en los agentes)
skills/            → copia en ~/.config/opencode/skills/
```

## Instalación (OpenCode)

```bash
git clone https://github.com/bouhamdi22us-arch/ai_agency.git
cd ai_agency

# Agentes y skills
mkdir -p ~/.config/opencode
cp -r agents/*   ~/.config/opencode/agents/
cp -r skills/*   ~/.config/opencode/skills/

# Biblioteca (ajusta las rutas en los agentes si la pones en otro sitio)
cp -r agency-library ~/agency-library
```

Las skills de terceros también pueden instalarse desde sus repos originales (recomendado,
para recibir actualizaciones): ver los enlaces en [CREDITS.md](CREDITS.md).

## Qué NO está aquí (y por qué)

- **`opencode.jsonc` / `service.json`** — la configuración local contiene credenciales
  (token de GitHub, contraseña de servicio). Publicarlas sería un fallo de seguridad, así que
  se excluyen a propósito. Usa `opencode.example.jsonc` como referencia.
- **`aos/queue.json`** — estado runtime local de la cola de tareas AOS.
- **`node_modules/`, `.git/` locales** — artefactos de build/estado.
- **Proyectos de cliente/propios** (`verttel`, `nexo-crm`) — no forman parte de la agencia;
  son productos separados y no se publican aquí.
- **`skills/prototype-ui`** — symlink roto en el origen (se autorreferenciaba); omitida.
- **`andrej-karpathy-skills`** — la skill `karpathy-guidelines` se incluye como referencia
  porque el upstream no muestra licencia; los derechos pertenecen a sus autores.

## La situación, honestamente

- El contenido propio (agentes + biblioteca + AOS) es original de este proyecto y se publica bajo MIT.
- Las skills de `skills/` son trabajo de otras personas; se redistribuyen **con atribución**
  en CREDITS.md y bajo sus licencias originales (MIT / Apache-2.0 en su mayoría). Si eres autor
  de alguna y prefieres que se retire, abre un issue.
- La biblioteca tiene partes marcadas como verificadas e interpretaciones propias; consulta
  `agency-library/MAINTENANCE.md` antes de ampliar.
- Esto es un sistema vivo, no un producto terminado: úsalo como base.

## Licencia

MIT para el contenido propio (ver [LICENSE](LICENSE)). Las skills de terceros conservan sus
licencias — ver [CREDITS.md](CREDITS.md).
