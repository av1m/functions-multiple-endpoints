from flask import Blueprint


bp = Blueprint("user", __name__, url_prefix="/user")

@bp.route("/<int:id>", methods=["GET"])
def change_account(id):
    return str(id), 200
