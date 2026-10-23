# spaced-repetition-app

Aplicación web local para memorizar con tarjetas y repetición espaciada. Admite dos modelos de tarjeta: básica con tarjeta invertida y básica de teclear la respuesta.

- Qué se espera de la app: [SPEC.md](SPEC.md)
- Cómo está hecha: [DESIGN.md](DESIGN.md)
- Casos de prueba acordados: [TEST-PLAN.md](TEST-PLAN.md)
- Temas pendientes: [TODO.md](TODO.md)

## Instalación

Desde la raíz del repositorio, prepara el entorno como indica [CONTRIBUTING.md](../../CONTRIBUTING.md#entorno-python):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
python learning/spaced-repetition-app/run.py
```

Se abre el navegador en `http://127.0.0.1:5000`. La primera vez aparece el manual de ayuda, que explica cómo trabajar con la app. Desde la barra superior se accede a **Progreso**, **Ayuda** y **Estudio libre**. Para terminar, pulsa **Ya vale por hoy**: el servidor se detiene y la terminal queda libre.

## Añadir tarjetas

Añade una fila a `data/cards.csv`. Se puede editar con cualquier editor de texto o con una hoja de cálculo. [data/cards-demo.csv](data/cards-demo.csv) es una plantilla comentada con un ejemplo de cada caso, y el formato completo está en [DESIGN.md](DESIGN.md#contenido-datacardscsv).

```csv
id,enabled,model,front,back,image
dog,true,reversed,Dog,Perro,
boe,true,typed,¿Qué significa BOE?,Boletín Oficial del Estado|Boletín Oficial,
poderes,true,typed,¿Cuáles son los tres poderes del Estado?,Legislativo|Parlamento;Ejecutivo;Judicial,
```

- `model`: `reversed` (piensas la respuesta, sale en las dos direcciones) o `typed` (tecleas la respuesta exacta).
- `back` en `typed`: `|` separa formas válidas (vale cualquiera) y `;` separa elementos de una lista (valen todos, en cualquier orden). En `reversed` se muestra tal cual.
- `enabled`: `false` oculta la nota sin borrarla ni perder su progreso.

Para asociarle una imagen de licencia libre, desde la raíz del repositorio:

```bash
python learning/spaced-repetition-app/scripts/fetch_images.py boe "Boletín Oficial del Estado"
```

- `boe`: id de la nota en `cards.csv` (primera columna).
- `"Boletín Oficial del Estado"`: qué buscar. Entre comillas si tiene espacios.

Por defecto busca en [Pixabay](https://pixabay.com/), cuyas fotos se pueden usar sin atribución, si hay clave de API. Sin clave, busca en [Openverse](https://openverse.org/), que reúne imágenes con licencia libre de Flickr, Wikimedia Commons y otras colecciones abiertas. En los dos casos descarga el primer resultado.

La clave de Pixabay es gratuita: se obtiene en la [documentación de su API](https://pixabay.com/api/docs/) y se guarda en `learning/spaced-repetition-app/.env`, que git ignora:

```bash
echo 'PIXABAY_API_KEY=tu-clave' > learning/spaced-repetition-app/.env
```
 Para elegir entre varios candidatos antes de descargar:

```bash
python learning/spaced-repetition-app/scripts/fetch_images.py boe "Boletín Oficial del Estado" --list 8 --preview-dir /tmp/previews
python learning/spaced-repetition-app/scripts/fetch_images.py boe "Boletín Oficial del Estado" --pick 3
```

- `--list 8`: muestra los 8 primeros candidatos (título, autor, licencia y origen) sin descargar nada.
- `--preview-dir`: con `--list`, guarda la miniatura de cada candidato para revisarla.
- `--pick 3`: descarga el candidato número 3 de la lista.
- `--source pixabay|openverse|wikimedia`: elige la fuente en lugar de la de por defecto.

Si el servidor responde que hay demasiadas peticiones, el script espera y lo reintenta.

Para pasar las tarjetas a Anki, en la pantalla Progreso pulsa Exportar para Anki y abre el fichero descargado en Anki (*Archivo → Importar*).

## Progreso local

> [!IMPORTANT]
> El progreso se guarda en `data/progress.json`, que **no se sube a git**. Solo existe en el equipo donde estudias. Si clonas el repositorio en otro equipo, empiezas de cero. Si borras el fichero, pierdes el progreso.

## Licencia

[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/), como el resto del repositorio, salvo las imágenes de `app/static/images/`. Proceden de Pixabay ([licencia de contenido de Pixabay](https://pixabay.com/service/license-summary/)), de Wikimedia Commons y de otras colecciones abiertas que indexa Openverse, y mantienen su licencia original (por ejemplo, CC BY-SA). El autor y la licencia de cada una están en [data/image-credits.md](data/image-credits.md).
