import os

from flask_cors import CORS
from flask_openapi3 import OpenAPI
from flask_sqlalchemy import SQLAlchemy

from app.api import blueprints

root_path = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()


def create_app():
    app = OpenAPI(__name__)
    app.config.from_object("app.config.DevelopmentConfig")

    for blueprint in blueprints:
        app.register_api(blueprint)

    CORS(app)
    # db.init_app(app)
    app.app_context().push()
    return app

