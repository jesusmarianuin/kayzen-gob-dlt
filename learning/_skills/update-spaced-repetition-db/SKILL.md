---
name: update-spaced-repetition-db
description: Genera y mantiene las tarjetas de learning/spaced-repetition-app/data/cards.tsv a partir del conocimiento del repositorio. Úsalo cuando el usuario pida crear, ampliar, corregir o revisar tarjetas de repetición espaciada. Es interactivo, el usuario decide el foco y aprueba cada tarjeta antes de escribirla.
---

# update-spaced-repetition-db

Construye la base de datos de tarjetas que usa la app de [learning/spaced-repetition-app](../../spaced-repetition-app/README.md). El agente propone y el usuario decide: el foco (qué temas, qué ficheros, cuántas tarjetas) lo marca siempre el usuario.

## Rutas que usa el skill

Todos los comandos se ejecutan desde la raíz del repositorio, con el entorno virtual activado (`source .venv/bin/activate`).

- `knowledge-base/` y `topics/`: fuentes de conocimiento
- `learning/spaced-repetition-app/data/cards.tsv`: base de datos de tarjetas que se actualiza
- `learning/spaced-repetition-app/data/`: carpeta que se copia en el backup
- `learning/spaced-repetition-app/DESIGN.md`: formato de `cards.tsv`, reglas del id y comparación de respuestas
- `learning/spaced-repetition-app/scripts/fetch_images.py`: descarga de imágenes
- `learning/_skills/update-spaced-repetition-db/log/`: backups, logs de cada pasada y propuestas

Estas rutas están autorizadas por el propio skill. Cualquier otra lectura sigue las normas de `AGENTS.md`.

## Fuentes de conocimiento

Salvo que el usuario indique otra cosa, las tarjetas salen de estas carpetas:

- `knowledge-base/`
- `topics/`

La lista crecerá a medida que aparezcan nuevas fuentes relevantes.

Las carpetas y ficheros cuyo nombre empieza por guion bajo (`_skills`, por ejemplo) son privados y no se usan como fuente, estén al nivel que estén.

## Flujo de una pasada

Todos los ficheros de una pasada comparten la misma marca de tiempo `YYYY-MM-DD-HH-MM` (por ejemplo, `2026-09-15-12-30`), fijada al empezar.

### 1. Acordar el alcance

Pregunta al usuario qué quiere trabajar si no lo ha dicho: carpetas o ficheros concretos, tema, número aproximado de tarjetas. Consulta los logs `.jsonl` anteriores de `log/` para saber qué fuentes ya se procesaron y cuáles han cambiado desde entonces (comparando el `sha256`).

### 2. Hacer el backup

Antes de tocar nada, copia toda la carpeta `data/` en un `.tar`:

```bash
TS=$(date +%Y-%m-%d-%H-%M)
tar -cf "learning/_skills/update-spaced-repetition-db/log/$TS.tar" -C learning/spaced-repetition-app data
tar -tf "learning/_skills/update-spaced-repetition-db/log/$TS.tar"
```

El segundo comando lista el contenido para verificar que el backup es correcto.

### 3. Proponer tarjetas

Lee las fuentes acordadas y escribe la propuesta en `log/proposals/<marca>.tsv`, con el formato de [Fichero de propuesta](#fichero-de-propuesta). Todas las filas nuevas llevan `decision` = `pending`. Muestra al usuario un resumen en una tabla (id, pregunta, respuesta, fuente) y la ruta del fichero.

Antes de proponer, revisa `cards.tsv` para no repetir conceptos ni ids ya existentes.

### 4. Revisión del usuario

El usuario marca cada fila como `include` o `discard` y puede corregir `front`, `back`, `alternatives` o `image_query`, en el chat o editando el fichero directamente. No sigas mientras queden filas en `pending`, salvo que el usuario diga qué hacer con ellas.

### 5. Escribir en `cards.tsv`

- Añade al final de `cards.tsv` las filas `include`, en el orden de la propuesta (el orden de las filas decide el orden en que salen las tarjetas nuevas).
- Aplica las filas `update` sobre la nota con ese id, sin cambiar el id.
- Las filas `discard` no se escriben, pero se quedan en la propuesta como registro.
- Si `cards.tsv` solo contiene las tarjetas de ejemplo (las mismas que `cards-demo.tsv`), sustitúyelas: deja la cabecera y escribe solo las tarjetas nuevas. `cards-demo.tsv` no se toca.

Valida el fichero después de escribirlo:

```bash
python -c "import sys; sys.path.insert(0, 'learning/spaced-repetition-app'); from app import storage; print(len(storage.load_notes()), 'notas OK')"
```

### 6. Buscar imágenes

Busca siempre una imagen para cada nota nueva, después de escribirla en `cards.tsv` (el script falla si la nota no existe):

```bash
python learning/spaced-repetition-app/scripts/fetch_images.py <id> "<término de búsqueda>"
```

El script descarga la imagen en `app/static/images/<id>.jpg`, rellena la columna `image` y añade el crédito a `data/image-credits.md`. Cómo elegir el término está en [Búsqueda de imágenes](#búsqueda-de-imágenes).

### 7. Guardar el log

Escribe `log/<marca>.jsonl` con el formato de [Log de la pasada](#log-de-la-pasada) y resume al usuario lo hecho: tarjetas añadidas, actualizadas y descartadas, e imágenes no encontradas.

## Redacción de las tarjetas

El formato completo de `cards.tsv` está en [DESIGN.md](../../spaced-repetition-app/DESIGN.md#contenido-datacardstsv). Criterios para redactar:

- Un solo concepto por tarjeta. Si una fuente da tres ideas, son tres tarjetas.
- Pregunta y respuesta en español. Los términos técnicos habituales del sector se mantienen en inglés, igual que en la documentación.
- Respuestas cortas: la app compara lo tecleado de forma literal (sin tildes ni mayúsculas, pero sin tolerar palabras distintas).
- `Basic (type in the answer)` para siglas, nombres de normas, organismos, fechas y cifras: respuestas con una forma exacta. Añade en `alternatives` las variantes aceptables separadas por `|` (por ejemplo, sin palabras de enlace o con el nombre abreviado).
- `Basic (and reversed card)` para pares término-definición breve que tenga sentido preguntar en los dos sentidos. Evítalo si la definición es larga: al invertirla no se puede recordar.
- No hagas tarjetas de datos efímeros de noticias (fechas de un evento, asistentes) salvo que el usuario lo pida. Prioriza conceptos, normas, organismos y relaciones entre ellos.
- id en kebab-case ASCII, único e inmutable (`^[a-z0-9]+(-[a-z0-9]+)*$`, máximo 40 caracteres). Hazlo descriptivo del concepto: `ens-categorias`, `eidas-2`, `dlt-definicion`.

## Búsqueda de imágenes

El repositorio es técnico y Wikimedia Commons no tiene fotos de conceptos abstractos. Buscar "imagen de IPFS" o "nodo blockchain" no da nada útil. Aplica esta escalera hasta obtener resultado:

1. Simplifica el concepto a algo fotografiable que lo evoque: "computer network" para IPFS o blockchain, "signature pen document" para firma electrónica, "padlock" para cifrado.
2. Si no hay resultado, busca algo más genérico que conecte con la idea: "person working computer", "server room", "office documents".
3. Si tampoco hay resultado, deja la nota sin imagen (la app usa un fondo neutro) y regístralo en el log.

Escribe los términos en inglés, porque Commons indexa sobre todo descripciones en inglés. Anota en la columna `image_query` de la propuesta el término que funcionó.

## Fichero de propuesta

Ruta: `learning/_skills/update-spaced-repetition-db/log/proposals/<marca>.tsv`. Separado por tabuladores, con una fila de cabecera y estas columnas:

| Columna | Contenido |
| --- | --- |
| `decision` | `pending`, `include`, `discard` o `update` |
| `id` | id de la nota. En `update`, el de una nota existente |
| `model` | `Basic (and reversed card)` o `Basic (type in the answer)` |
| `front` | Pregunta |
| `back` | Respuesta |
| `alternatives` | Respuestas alternativas separadas por `\|`. Puede quedar vacía |
| `image_query` | Término de búsqueda para `fetch_images.py` |
| `source` | Ruta del fichero fuente |
| `notes` | Motivo del descarte o comentario del usuario |

Para corregir tarjetas ya existentes (una respuesta errónea detectada al estudiar, por ejemplo), crea una propuesta con filas `update` que lleven el id existente y los campos corregidos. El progreso se conserva porque el id no cambia.

## Log de la pasada

Ruta: `learning/_skills/update-spaced-repetition-db/log/<marca>.jsonl`. Una línea JSON por fichero fuente revisado, usado o descartado:

```json
{"source": "topics/ens/ABOUT.md", "sha256": "3f2a...", "status": "used", "reason": "", "proposal": "proposals/2026-09-15-12-30.tsv", "included": ["ens-categorias"], "discarded": ["ens-fecha-rev"], "no_image": []}
```

- `status`: `used` si salió alguna tarjeta, `discarded` si se revisó y no aporta, `skipped` si quedó fuera del alcance de la pasada.
- `reason`: obligatorio en `discarded` y `skipped`.
- `sha256`: huella del fichero (`sha256sum <fichero>`), para detectar en la siguiente pasada si ha cambiado.

Así otra sesión puede retomar el trabajo sin empezar de cero y se puede auditar si algo quedó fuera por error.

## Prompts de ejemplo

- "Genera tarjetas del glosario de `knowledge-base/glossary.md`, unas 20."
- "Crea tarjetas sobre las categorías y medidas del ENS a partir de `topics/ens`."
- "Revisa las noticias de PAE de 2026 sobre identidad digital y propón tarjetas solo de conceptos y normas."
- "¿Qué fuentes han cambiado desde la última pasada? Propón tarjetas solo de lo nuevo."
- "La tarjeta `eidas-2` tiene mal la respuesta, corrígela."

## Resolución de problemas

- `cards.tsv línea N: id duplicado`: el id ya existe. Cambia el id de la fila nueva, nunca el de la existente.
- `no existe ninguna nota con id`: `fetch_images.py` se lanzó antes de escribir la nota en `cards.tsv`.
- `No se ha encontrado ninguna imagen JPEG`: sube un escalón en [Búsqueda de imágenes](#búsqueda-de-imágenes).
- Error de red en `fetch_images.py`: la tarjeta ya está escrita. Deja la imagen pendiente, anótala en `no_image` y reinténtalo en otra pasada.
- Hay que deshacer una pasada: restaura el backup con `tar -xf learning/_skills/update-spaced-repetition-db/log/<marca>.tar -C learning/spaced-repetition-app`. Las imágenes descargadas en `app/static/images/` no están en el backup y hay que borrarlas a mano.

---

