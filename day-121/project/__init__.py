from flask import Flask

from .config import config
from . import models, routes

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    models.init_app(app)
    routes.init_app(app)
    
    return app
