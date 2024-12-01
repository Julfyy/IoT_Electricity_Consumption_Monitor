from flask import Flask
from .config import Config
from .database import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ініціалізація бази даних
    init_db(app)

    # Реєстрація маршрутів
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
