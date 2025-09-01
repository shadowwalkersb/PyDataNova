from flask import Blueprint

bp = Blueprint("users-mock", __name__)

@bp.route("/", methods=["GET"])
def get_users():
    return [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"},
    ]
