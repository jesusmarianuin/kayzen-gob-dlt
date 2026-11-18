---
name: get-inza-posts
description: Buscar posts de inza.blog por año o mes, presentar un log de revisión para que el usuario elija qué incluir (no incluir, bajo interés, alto interés) y redactar los elegidos en knowledge-base/inza.blog/. Usar siempre que se pida bajar, revisar o actualizar posts de inza.blog, aunque no se mencione el script.
---

# get-inza-posts

Herramientas de meta-trabajo para `knowledge-base/inza.blog/`.

Invocar esta skill autoriza a leer `knowledge-base/inza.blog/` y la carpeta de la propia skill.

Las decisiones de diseño están en [design-notes.md](design-notes.md).

## Lanzar el script

Entorno: el mismo `.venv` de [CONTRIBUTING.md](../../../CONTRIBUTING.md). Los comandos se lanzan desde la raíz del repositorio.

```bash
python .claude/skills/get-inza-posts/scripts/get_inza_posts.py month 2026 10
python .claude/skills/get-inza-posts/scripts/get_inza_posts.py year 2026
python .claude/skills/get-inza-posts/scripts/get_inza_posts.py month 2026 10 --words 0
```

El periodo lo indica el usuario en el prompt ("baja 2026", "baja octubre de 2026"). `year` recorre los doce meses por su cuenta, con una petición por mes; no hace falta ir mes a mes desde el agente.

Salida: una línea por post. Cada línea un JSON con:

- `url`, `title`, `date`, `categories`
- `file`: ruta del documento que le corresponde (`knowledge-base/inza.blog/AAAA/MM/DD-<slug>.md`)
- `ya_bajado`: si ya existe el documento de `file`
- `links`: enlaces que cita el post, sin las imágenes del propio blog
- `body`: las primeras 300 palabras del texto; `--words N` para otra cantidad, `--words 0` para el texto completo

El script solo busca: no decide qué se incluye ni escribe documentos.

## Flujo de trabajo

- Ejecutar el script para el periodo pedido
- Descartar los posts con `ya_bajado: true` y los que un log anterior de `log/` tenga con `nivel_final: no-incluir`
- Guardar el log (ver "Log") con el resto y presentar el `-review.md` al usuario
- Esperar a que el usuario lo devuelva marcado
- Volver a ejecutar el script para el mismo periodo con `--words 0` y redactar solo los posts marcados con `[b]` o `[a]`
- Actualizar `nivel_final` en el `.jsonl` con la marca del usuario

## Log

Al acabar una pasada, guardar en `.claude/skills/get-inza-posts/log/`:

- `AAAA-MM-DD-<alcance>.jsonl` (por ejemplo, `2026-10-23-month-2026-10.jsonl`): una línea JSON por post con `url`, `title`, `date`, `ya_bajado` y `nivel_final` (`null` hasta que el usuario marque; después `no-incluir`, `bajo` o `alto`)
- `AAAA-MM-DD-<alcance>-review.md`: una línea por post propuesto, todas en `[ ]`

Formato de cada línea del `-review.md`:

```markdown
- [ ] 2026-10-22 — [Cuando la criptografía era un arma: de los 40 bits y el SGC a la criptoagilidad](https://inza.blog/2026/10/22/cuando-la-criptografia-era-un-arma-de-los-40-bits-y-el-sgc-a-la-criptoagilidad/)
```

El usuario cambia `[ ]` (no incluir) por `[b]` (bajo interés) o `[a]` (alto interés). No hay criterio de interés previo: el agente no propone niveles.

## Formato del documento

Ruta y nombre: el campo `file` de la salida del script.

```markdown
# <título original del post>

Post: <https://inza.blog/AAAA/MM/DD/slug/>

Fecha: AAAA-MM-DD

<resumen o explicación, con los enlaces de referencia del post en línea>

En una frase: <síntesis del post>

---
```

- Sin front matter de clasificación
- Los enlaces de referencia salen del campo `links` y se integran en el texto donde correspondan, como en las fichas de `scrape-pae-news` (por ejemplo, [2026-03-13-CRED-MITOS.md](../../../knowledge-base/pae-news/2026/2026-03-13-CRED-MITOS.md))
- Bajo interés: resumen sin interpretar, en base al artículo, de varios párrafos como corresponda pero sin superar 200 palabras.
- Alto interés: resumen sin interpretar, en base al artículo, de varios párrafos como corresponda pero sin superar 500 palabras.
