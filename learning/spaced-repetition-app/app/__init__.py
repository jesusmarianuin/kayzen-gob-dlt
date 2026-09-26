"""Flask application factory."""

import os
from collections.abc import Callable

from flask import Flask


def create_app(shutdown: Callable[[], None] | None = None) -> Flask:
    """Create the app. `shutdown` stops the server when the user presses "Ya vale por hoy"."""
    app = Flask(__name__)
    # La sesión solo guarda el orden del estudio libre; basta una clave nueva en cada arranque
    app.secret_key = os.urandom(16)
    app.config["SHUTDOWN"] = shutdown

    from app import routes
    routes.register(app)
    return app
