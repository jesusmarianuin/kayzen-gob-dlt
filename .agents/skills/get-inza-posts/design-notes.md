# Diseño de get-inza-posts

## Objetivo

Skill para descargar los posts de [inza.blog](https://inza.blog/) de un periodo indicado en el prompt (un año o un mes). Antes de descargar, el usuario elige qué posts incluir mediante un log de revisión. Por cada post elegido se genera un documento markdown en `knowledge-base/inza.blog/AAAA/MM/`.

Sigue el mismo esquema que `scrape-pae-news`: el script busca, el agente registra el log, el usuario marca y el agente redacta solo lo marcado.

## Decisiones de diseño

### Estructura de la skill

```plaintext
.claude/skills/get-inza-posts/
├── SKILL.md
├── design-notes.md
├── scripts/
│   └── get_inza_posts.py
└── log/
    ├── AAAA-MM-DD-<alcance>.jsonl
    └── AAAA-MM-DD-<alcance>-review.md
```

### Script

Se lanza desde la raíz del repositorio con el `.venv` de [CONTRIBUTING.md](../../../CONTRIBUTING.md):

```bash
python .claude/skills/get-inza-posts/scripts/get_inza_posts.py month 2026 10
python .claude/skills/get-inza-posts/scripts/get_inza_posts.py year 2026
```

Comportamiento:

- Pide los posts del periodo a la API pública de WordPress.com (`https://public-api.wordpress.com/rest/v1.1/sites/inza.blog/posts/` con `after` y `before`), que devuelve título, URL, fecha, categorías y texto completo
- Pide los posts mes a mes: `month` hace una petición y `year` recorre internamente los doce meses, una petición por mes
- Si un mes superase los 100 posts que la API devuelve como máximo por petición, el script avisa
- Espera entre peticiones para no saturar el servicio
- Salida: una línea JSON por post con `url`, `title`, `date`, `categories`, `file` (ruta del documento que le corresponde), `ya_bajado`, `links` (enlaces que cita el post, sin las imágenes del propio blog) y `body` (primeras 300 palabras, las que indique `--words N`, o el texto completo con `--words 0`)
- El script solo busca: no decide qué se incluye ni escribe documentos

### Evitar descargas repetidas

- Se considera bajado un post cuyo documento (`file`) ya existe. No basta con que su URL aparezca en algún `.md`, porque los documentos citan otros posts del blog que no se han redactado
- Los posts marcados como "no incluir" quedan en el `.jsonl` y no se vuelven a proponer

### Log

No hay criterio de interés previo: todo el contenido del sitio se considera de interés y la selección la hace el usuario.

El `.jsonl` guarda una línea por post encontrado, con:

- `url`, `title`, `date`
- `ya_bajado`: si ya existía documento para esa URL antes de la pasada
- `nivel_final`: `no-incluir`, `bajo` o `alto`, según la marca del usuario

El `-review.md` presenta una línea por post. Todas empiezan en `[ ]` (no incluir), y el usuario las cambia a `[b]` (bajo interés) o `[a]` (alto interés):

```markdown
- [ ] 2026-10-22 — [Cuando la criptografía era un arma: de los 40 bits y el SGC a la criptoagilidad](https://inza.blog/2026/10/22/cuando-la-criptografia-era-un-arma-de-los-40-bits-y-el-sgc-a-la-criptoagilidad/)
```

El agente redacta documentos solo para las líneas marcadas con `[b]` o `[a]`.

### Documento generado

- Ruta: `knowledge-base/inza.blog/AAAA/MM/DD-<slug>.md`
- Nombre: el día de publicación como prefijo y el slug de la URL del post (ya en kebab-case y en minúsculas, derivado del título original), tal como lo devuelve la API. Por ejemplo, `22-cuando-la-criptografia-era-un-arma-de-los-40-bits-y-el-sgc-a-la-criptoagilidad.md`
- Sin front matter de clasificación
- Contenido común a ambos niveles: título original, enlace original bien visible, fecha de publicación y enlaces de referencia que cita el post, integrados en el texto
- Bajo interés: resumen sin interpretar, en base al artículo, de varios párrafos como corresponda pero sin superar 200 palabras
- Alto interés: resumen sin interpretar, en base al artículo, de varios párrafos como corresponda pero sin superar 500 palabras

Formato, tomado de las fichas de `scrape-pae-news` (por ejemplo, [2026-03-13-CRED-MITOS.md](../../../knowledge-base/pae-news/2026/2026-03-13-CRED-MITOS.md)):

```markdown
# <título original del post>

Post: <https://inza.blog/AAAA/MM/DD/slug/>

Fecha: AAAA-MM-DD

<resumen o explicación, con los enlaces de referencia del post en línea>

En una frase: <síntesis del post>

---
```
