"""Flask application factory."""

import os
from collections.abc import Callable

from flask import Flask


def create_app(shutdown: Callable[[], None] | None = None) -> Flask:
    """Create the app. `shutdown` stops the server when the user presses "Ya vale por hoy"."""
    app = Flask(__name__)
    # La sesión guarda el área elegida y el orden del estudio libre. Con una clave nueva en cada
    # arranque se pierde al cerrar, así que cada vez que se abre la app se elige área
    app.secret_key = os.urandom(16)
    app.config["SHUTDOWN"] = shutdown

    from app import routes
    routes.register(app)
    return app
