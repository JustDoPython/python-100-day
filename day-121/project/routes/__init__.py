from .home import home_bp
from .profile import profile_bp

def init_app(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(profile_bp)