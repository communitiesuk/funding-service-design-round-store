"""The entry point for app.py to start our app
"""
from api import api
from flask import Flask


def create_app() -> Flask:

    flask_app = Flask(__name__)
    api.register(flask_app)
    api.config.title = "Round Store API"
    api.config.version = "0.1"
    api.config.mode = "strict"
    api.config.description = (
        "An api for requesting information about rounds for DLUHC funding"
    )

    from api.endpoints import rounds_bp

    flask_app.register_blueprint(rounds_bp)

    return flask_app


app = create_app()
