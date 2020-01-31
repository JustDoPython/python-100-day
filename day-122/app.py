from flask import Flask, request
from config import config
from route import route_bp
from model import init_app

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    init_app(app)
    app.register_blueprint(route_bp)
    return app

    