"""Entry point: start the local server and open the browser.

Usage (from the repository root):
    python learning/spaced-repetition-app/run.py [--no-browser]
"""

import sys
import threading
import webbrowser
from pathlib import Path

# Permite ejecutar el script desde cualquier directorio
sys.path.insert(0, str(Path(__file__).resolve().parent))

from werkzeug.serving import make_server  # noqa: E402

from app import config, create_app, storage  # noqa: E402


def main() -> int:
    try:
        storage.load_notes()
    except storage.CardsFileError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    server = None
    app = create_app(shutdown=lambda: server.shutdown())
    try:
        server = make_server(config.HOST, config.PORT, app, threaded=True)
    except OSError as error:
        print(f"Error: no se puede usar el puerto {config.PORT} ({error}). "
              "¿Está la app ya abierta en otra terminal?", file=sys.stderr)
        return 1

    url = f"http://{config.HOST}:{config.PORT}"
    print(f"App en {url}. Para terminar, pulsa \"Ya vale por hoy\" o Ctrl+C.")
    if "--no-browser" not in sys.argv:
        threading.Timer(0.5, webbrowser.open, args=(url,)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    print("Hasta mañana.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
