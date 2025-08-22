from flask import Blueprint, request, jsonify
from api.core.services import users as users_service
from api.core.utils.logger import get_logger
from api.core.utils.validation import validate_payload

logger = get_logger()
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

@bp.route("/", methods=["POST"])
def create_user():
    db = request.args.get("db")
    payload = request.json
    try:
        validate_payload(["name", "email"], payload)
        return jsonify(users_service.create_user(db, payload))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    db = request.args.get("db")
    payload = request.json
    return jsonify(users_service.update_user(db, user_id, payload))

@bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    db = request.args.get("db")
    return jsonify(users_service.delete_user(db, user_id))
