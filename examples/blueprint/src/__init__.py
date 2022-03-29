from flask import Flask
from src import user


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user.bp)

    @app.route("/")
    def _():
        return "Hello, World!", 200

    return app

