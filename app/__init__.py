# app/__init__.py
from flask import Flask, render_template
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints here
    from app.routes.auth_routes import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    # Simple test route (optional, can be removed later)
    @app.route('/hello')
    def hello():
        return "Hello, World!"

    return app