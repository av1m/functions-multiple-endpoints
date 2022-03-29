from flask import Flask
from functions_wrapper import entrypoint

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!", 200


@app.route("/user/<int:id>", methods=["GET"])
def user(id):
    return f"Hello {id}!", 200


app_wrap = lambda request: entrypoint(app, request)

# Run with the following command:
# functions_framework --target app_wrap