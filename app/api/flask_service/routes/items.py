from flask import Blueprint

bp = Blueprint("items", __name__)

@bp.route("/", methods=["GET"])
def get_items():
    return []
