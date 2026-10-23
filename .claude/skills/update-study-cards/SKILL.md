---
name: update-study-cards
description: Revisa las tarjetas de repaso de cards.csv frente a un documento fuente, propone preguntas que faltan, asigna los id vacíos y busca imágenes libres para las tarjetas sin imagen.
argument-hint: "<documento-fuente.md> [ruta-cards.csv]"
---

# Actualizar tarjetas de repaso

Tarea sobre la app de [repetición espaciada](../../../learning/spaced-repetition-app/README.md) a partir de un documento fuente.

## Entradas

- Primer argumento: documento fuente del que salen las tarjetas (por ejemplo, `knowledge-base/blockchain.md`)
- Segundo argumento, opcional: fichero de tarjetas. Por defecto, `learning/spaced-repetition-app/data/cards.csv`
- Argumentos recibidos: `$ARGUMENTS`

Si falta el documento fuente, pregunta por él antes de empezar.

## Permisos de lectura

Invocar esta skill autoriza a leer:

- El documento fuente indicado
- La carpeta `learning/spaced-repetition-app/`, con todo lo que contiene

Cualquier otra lectura sigue las normas de AGENTS.md: si falta información, pregunta.

## Reglas comunes

- No hagas ninguna operación git
- El formato de `cards.csv` está en `data/cards-demo.csv` y en `app/storage.py`: respétalo (cabecera, comillas dobles si el texto lleva comas, `;` para listas y `|` para alternativas en `typed`)
- No cambies nunca un id que ya exista: el progreso de `data/progress.json` está asociado a él
- No modifiques el texto de las tarjetas existentes salvo que el usuario lo pida. Si ves erratas o respuestas `typed` imposibles de teclear con exactitud, avisa en el chat
- El criterio para elegir `reversed` o `typed` está en `SPEC.md` (sección "Modelos elegidos")

## Paso 1: proponer preguntas que faltan

1. Lee el documento fuente y `cards.csv`.
2. Detecta las ideas del documento que no cubre ninguna tarjeta.
3. Propón en el chat una lista numerada. Para cada propuesta, indica:
   - Modelo (`reversed` o `typed`) y por qué
   - Frente
   - Reverso, en el formato que tendrá en el CSV
   - Sección del documento de la que sale
4. Detente y espera a que el usuario elija los números. No añadas nada sin su elección.
5. Añade al final de `cards.csv` las elegidas, con `enabled` a `true` y la columna `image` vacía.

Si el documento ya está cubierto, dilo y pasa al paso 2.

## Paso 2: asignar los id que faltan

Para cada fila con el id vacío, escribe uno que:

- Esté en inglés y en kebab-case: minúsculas sin tildes, dígitos y guiones
- Tenga como máximo 40 caracteres
- Describa el concepto de la tarjeta, no su posición (`blockchain-design`, no `card-3`)
- No coincida con ningún otro id del fichero

## Paso 3: buscar imágenes

Las imágenes salen de Pixabay. El script lee la clave de `learning/spaced-repetition-app/.env` (`PIXABAY_API_KEY=...`); si falta, pídela al usuario.

Para cada fila con `enabled` distinto de `false` y la columna `image` vacía:

1. Busca con un término sencillo, en inglés, que describa un objeto o una escena concreta. Los conceptos técnicos (blockchain, QBFT, sharding) no dan resultados útiles, así que tradúcelos a algo que se pueda fotografiar:
   - Descentralización: `honeycomb bees`
   - Equilibrio entre tres propiedades: `stacked stones balance`
   - Bifurcación: `railway switch`
   - Red entre países: `europe map`
   - Tipos o variantes: `doors`
   - Encadenamiento: `chain links`
2. Lista 8 candidatos sin descargar, desde la raíz del repositorio y con el entorno Python de la app activo (ver README de la app):

   ```bash
   python learning/spaced-repetition-app/scripts/fetch_images.py <note_id> "<término>" --list 8 --preview-dir <scratchpad>/preview
   ```

3. Mira las miniaturas y elige la que mejor represente el concepto de la tarjeta. Descarta las que tengan texto que revele la respuesta, logotipos de marcas, símbolos de criptomonedas o personas reconocibles en primer plano.
4. Descarga la elegida:

   ```bash
   python learning/spaced-repetition-app/scripts/fetch_images.py <note_id> "<término>" --pick <número>
   ```

   Guarda `app/static/images/<note_id>.jpg`, escribe el nombre en la columna `image` y añade el autor y la licencia a `data/image-credits.md`.
5. Si ningún candidato encaja, busca con otro término. Haz como máximo 3 búsquedas por tarjeta; si ninguna sirve, deja la columna vacía y avisa en el chat.

## Paso 4: verificar

Comprueba que el fichero carga sin errores, desde la raíz del repositorio:

```bash
cd learning/spaced-repetition-app && python -c "from app import storage; print(len(storage.load_notes()), 'notas')"
```

Termina con un resumen en el chat:

- Tarjetas añadidas
- Id asignados
- Imagen elegida para cada tarjeta, con el término que la encontró
- Tarjetas sin imagen y avisos sobre erratas o respuestas dudosas
