# Diseño de get-edpb-news

## Objetivo

Skill para descargar las noticias del [European Data Protection Board](https://www.edpb.europa.eu/news_en) (EDPB) de un periodo indicado en el prompt (un año o un mes). Antes de descargar, el usuario elige qué noticias incluir mediante un log de revisión. Por cada noticia elegida se genera un documento markdown en `knowledge-base/edpb.europa.eu/AAAA/MM/`.

Sigue el mismo esquema que `get-inza-posts` y `scrape-pae-news`: el script busca, el agente registra el log, el usuario marca y el agente redacta solo lo marcado.

## Decisiones de diseño

### Estructura de la skill

```plaintext
.claude/skills/get-edpb-news/
├── SKILL.md
├── design-notes.md
├── scripts/
│   └── get_edpb_news.py
└── log/
    ├── AAAA-MM-DD-<alcance>.jsonl
    └── AAAA-MM-DD-<alcance>-review.md
```

### Fuente: listado HTML en lugar del feed RSS

La web publica un feed RSS en `/feed/news_en`, pero responde con un error 503 a los clientes automáticos, con cualquier User-Agent. El listado `https://www.edpb.europa.eu/news_en?page=N` sí responde, y además el feed solo trae noticias recientes, mientras que el listado permite llegar a cualquier periodo.

Características del listado que usa el script:

- 16 noticias por página, de la más reciente a la más antigua
- Cada tarjeta trae título, fecha (`<time datetime>`), tipo (`EDPB News` o `National News`), códigos de país en las nacionales y enlace a la noticia
- El listado mezcla noticias del EDPB y de las autoridades nacionales; el tipo y el país se guardan para que el usuario los vea en la revisión
- La página de cada noticia trae el cuerpo completo, los enlaces que cita y los temas asignados

### Script

Se lanza desde la raíz del repositorio con el `.venv` de [CONTRIBUTING.md](../../../CONTRIBUTING.md):

```bash
python .claude/skills/get-edpb-news/scripts/get_edpb_news.py month 2026 10
python .claude/skills/get-edpb-news/scripts/get_edpb_news.py year 2026
```

Comportamiento:

- Recorre el listado página a página y se detiene en cuanto la última noticia de una página es anterior al periodo pedido
- Por cada noticia del periodo pide su página para sacar el cuerpo, los enlaces y los temas
- Espera entre peticiones para no saturar el servicio y reintenta ante errores
- Salida: una línea JSON por noticia, en orden cronológico, con `url`, `title`, `date`, `type`, `countries`, `topics`, `file` (ruta del documento que le corresponde), `ya_bajado`, `links` y `body` (primeras 300 palabras, las que indique `--words N`, o el texto completo con `--words 0`)
- El script solo busca: no decide qué se incluye ni escribe documentos

### Evitar descargas repetidas

- Se considera bajada una noticia cuyo documento (`file`) ya existe
- Las noticias marcadas como "no incluir" quedan en el `.jsonl` y no se vuelven a proponer

### Log

No hay criterio de interés previo: la selección la hace el usuario.

El `.jsonl` guarda una línea por noticia encontrada, con:

- `url`, `title`, `date`, `type`, `countries`
- `ya_bajado`: si ya existía documento para esa URL antes de la pasada
- `nivel_final`: `no-incluir`, `bajo` o `alto`, según la marca del usuario

El `-review.md` presenta una línea por noticia, en español: tipo entre corchetes (`EDPB`, `Nacional` o `Ventanilla única`) para distinguir de un vistazo las del EDPB de las nacionales, título traducido y temas traducidos al final para poder filtrar por ellos. Todas empiezan en `[ ]` (no incluir), y el usuario las cambia a `[b]` (bajo interés) o `[a]` (alto interés):

```markdown
- [ ] 2026-11-13 — [EDPB] [El EDPB apoya el uso de otros modelos de cláusulas contractuales para transferencias ulteriores de datos personales](https://www.edpb.europa.eu/news/edpb-supports-use-of-other-models-of-contractual-clauses-for-onward-transfers-of-personal-data_en) — temas: instrumentos de transferencia y excepciones, cláusulas contractuales tipo
- [ ] 2026-11-17 — [Nacional · ie] [La autoridad irlandesa multa a MTCH con 11 millones de EUR tras investigar las solicitudes de datos de usuarios de Tinder](https://www.edpb.europa.eu/news/irish-data-protection-commission-fines-mtch-eur-11-million-following-inquiry-into-tinder-users_en) — temas: multas, aplicación del RGPD, derechos de los interesados
```

Como referencia de volumen, 2026 hasta noviembre tiene unas 70 noticias, la mitad nacionales.

El agente redacta documentos solo para las líneas marcadas con `[b]` o `[a]`.

### Documento generado

- Ruta: `knowledge-base/edpb.europa.eu/AAAA/MM/DD-<slug>.md`
- Nombre: el día de publicación como prefijo y el último tramo de la URL sin el sufijo de idioma (`_en`), que ya va en kebab-case. Por ejemplo, `13-edpb-supports-use-of-other-models-of-contractual-clauses-for-onward-transfers-of-personal-data.md`
- Sin front matter de clasificación
- Contenido común a ambos niveles: título original, enlace original bien visible, fecha de publicación, tipo de noticia y enlaces de referencia que cita, integrados en el texto
- La fuente solo existe en inglés (la versión `_es` de la web devuelve el mismo texto), así que el agente traduce: título, resumen y frase final en español, y el título original queda como referencia en una línea propia
- Bajo interés: resumen sin interpretar, en base a la noticia, de varios párrafos como corresponda pero sin superar 200 palabras
- Alto interés: resumen sin interpretar, en base a la noticia, de varios párrafos como corresponda pero sin superar 500 palabras

Formato, tomado de las fichas de `scrape-pae-news` (por ejemplo, [2026-03-13-CRED-MITOS.md](../../../knowledge-base/pae-news/2026/2026-03-13-CRED-MITOS.md)):

```markdown
# <título traducido al español>

Noticia: <https://www.edpb.europa.eu/news/slug_en>

Título original: <título en inglés, tal como aparece en la web>

Fecha: AAAA-MM-DD

Tipo: <noticia del EDPB | noticia nacional (código de país) | ventanilla única>

<resumen en español, con los enlaces de referencia de la noticia en línea>

En una frase: <síntesis de la noticia en español>

---
```
