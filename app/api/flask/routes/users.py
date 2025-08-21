from flask import Blueprint, request, jsonify
from api.core.services import users as users_service

bp = Blueprint("users", __name__)

@bp.route("/", methods=["GET"])
def get_users():
    db = request.args.get("db")
    return jsonify(users_service.get_all_users(db))

@bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    db = request.args.get("db")
    user = users_service.get_user_by_id(db, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)
