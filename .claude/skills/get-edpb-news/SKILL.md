---
name: get-edpb-news
description: Buscar noticias del EDPB (edpb.europa.eu) por año o mes, presentar un log de revisión para que el usuario elija qué incluir (no incluir, bajo interés, alto interés) y redactar las elegidas en knowledge-base/edpb.europa.eu/. Usar siempre que se pida bajar, revisar o actualizar noticias del EDPB o del Comité Europeo de Protección de Datos, aunque no se mencione el script.
---

# get-edpb-news

Herramientas de meta-trabajo para `knowledge-base/edpb.europa.eu/`.

Invocar esta skill autoriza a leer `knowledge-base/edpb.europa.eu/` y la carpeta de la propia skill.

Las decisiones de diseño están en [design-notes.md](design-notes.md).

## Idioma

La web del EDPB publica las noticias solo en inglés (la versión `_es` devuelve el mismo texto en inglés). Todo lo que produce esta skill va en español:

- En el `-review.md`: títulos, etiquetas de tipo y temas traducidos al español
- En cada documento: título traducido al español, resumen y frase final en español
- El título original en inglés solo aparece como referencia en el documento, en la línea "Título original"
- Siglas en su forma española: RGPD (GDPR), SEPD (EDPS), EIPD (DPIA), AEPD; se mantienen EDPB, CNIL, BCR y similares sin traducción habitual
- El `.jsonl` guarda los datos tal como los da el script, con el título original

## Lanzar el script

Entorno: el mismo `.venv` de [CONTRIBUTING.md](../../../CONTRIBUTING.md). Los comandos se lanzan desde la raíz del repositorio.

```bash
python .claude/skills/get-edpb-news/scripts/get_edpb_news.py month 2026 10
python .claude/skills/get-edpb-news/scripts/get_edpb_news.py year 2026
python .claude/skills/get-edpb-news/scripts/get_edpb_news.py month 2026 10 --words 0
```

El periodo lo indica el usuario en el prompt ("baja 2026", "baja octubre de 2026"). El script recorre por su cuenta las páginas del listado que hagan falta; no hace falta ir página a página desde el agente.

Salida: una línea por noticia. Cada línea un JSON con:

- `url`, `title`, `date`
- `type`: `EDPB News` (noticias del propio EDPB), `National News` (resoluciones y noticias de las autoridades nacionales) o `One-Stop-Shop News` (casos de ventanilla única)
- `countries`: códigos de país de la autoridad nacional, vacío en las noticias del EDPB
- `topics`: temas que la web asigna a la noticia
- `file`: ruta del documento que le corresponde (`knowledge-base/edpb.europa.eu/AAAA/MM/DD-<slug>.md`)
- `ya_bajado`: si ya existe el documento de `file`
- `links`: enlaces que cita el cuerpo de la noticia
- `body`: las primeras 300 palabras del texto; `--words N` para otra cantidad, `--words 0` para el texto completo

El script solo busca: no decide qué se incluye ni escribe documentos.

## Flujo de trabajo

- Ejecutar el script para el periodo pedido
- Descartar las noticias con `ya_bajado: true` y las que un log anterior de `log/` tenga con `nivel_final: no-incluir`
- Guardar el log (ver "Log") con el resto y presentar el `-review.md` al usuario
- Esperar a que el usuario lo devuelva marcado
- Volver a ejecutar el script para el mismo periodo con `--words 0` y redactar solo las noticias marcadas con `[b]` o `[a]`
- Actualizar `nivel_final` en el `.jsonl` con la marca del usuario

## Log

Al acabar una pasada, guardar en `.claude/skills/get-edpb-news/log/`:

- `AAAA-MM-DD-<alcance>.jsonl` (por ejemplo, `2026-11-18-month-2026-11.jsonl`): una línea JSON por noticia con `url`, `title`, `date`, `type`, `countries`, `ya_bajado` y `nivel_final` (`null` hasta que el usuario marque; después `no-incluir`, `bajo` o `alto`)
- `AAAA-MM-DD-<alcance>-review.md`: una línea por noticia propuesta, todas en `[ ]`

El `-review.md` empieza con un título, la fecha de generación con enlace al `.jsonl` y la leyenda de marcas, como los logs de `get-inza-posts`. Formato de cada línea, en español: el tipo entre corchetes (`EDPB`, `Nacional` o `Ventanilla única`, con el código de país cuando se conoce), el título traducido y, al final, los temas traducidos si los hay:

```markdown
- [ ] 2026-11-13 — [EDPB] [El EDPB apoya el uso de otros modelos de cláusulas contractuales para transferencias ulteriores de datos personales](https://www.edpb.europa.eu/news/edpb-supports-use-of-other-models-of-contractual-clauses-for-onward-transfers-of-personal-data_en) — temas: instrumentos de transferencia y excepciones, cláusulas contractuales tipo
- [ ] 2026-11-17 — [Nacional · ie] [La autoridad irlandesa multa a MTCH con 11 millones de EUR tras investigar las solicitudes de datos de usuarios de Tinder](https://www.edpb.europa.eu/news/irish-data-protection-commission-fines-mtch-eur-11-million-following-inquiry-into-tinder-users_en) — temas: multas, aplicación del RGPD, derechos de los interesados
```

Los temas permiten que el usuario filtre por ellos si el volumen del periodo es alto.

El usuario cambia `[ ]` (no incluir) por `[b]` (bajo interés) o `[a]` (alto interés). No hay criterio de interés previo: el agente no propone niveles.

## Formato del documento

Ruta y nombre: el campo `file` de la salida del script.

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

- Sin front matter de clasificación
- Todo el documento en español salvo la línea "Título original" (ver "Idioma")
- Los enlaces de referencia salen del campo `links` y se integran en el texto donde correspondan, como en las fichas de `scrape-pae-news` (por ejemplo, [2026-03-13-CRED-MITOS.md](../../../knowledge-base/pae-news/2026/2026-03-13-CRED-MITOS.md))
- Bajo interés: resumen sin interpretar, en base a la noticia, de varios párrafos como corresponda pero sin superar 200 palabras.
- Alto interés: resumen sin interpretar, en base a la noticia, de varios párrafos como corresponda pero sin superar 500 palabras.
