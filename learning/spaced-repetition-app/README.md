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

Añade una fila a `data/cards.tsv` (formato e id en [DESIGN.md](DESIGN.md#contenido-datacardstsv)). Para asociarle una imagen de Wikimedia Commons:

```bash
python learning/spaced-repetition-app/scripts/fetch_images.py boe "Boletín Oficial del Estado"
```

- `boe`: id de la nota en `cards.tsv` (primera columna).
- `"Boletín Oficial del Estado"`: qué buscar en Wikimedia Commons. Entre comillas si tiene espacios.

`data/cards.tsv` se puede importar en Anki (*Archivo → Importar*).

## Progreso local

> [!IMPORTANT]
> El progreso se guarda en `data/progress.json`, que **no se sube a git**. Solo existe en el equipo donde estudias. Si clonas el repositorio en otro equipo, empiezas de cero. Si borras el fichero, pierdes el progreso.

## Licencia

[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/), como el resto del repositorio, salvo las imágenes de `app/static/images/`. Proceden de Wikimedia Commons y mantienen su licencia original (por ejemplo, CC BY-SA). El autor y la licencia de cada una están en [data/image-credits.md](data/image-credits.md).
