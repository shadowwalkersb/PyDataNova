from flask import Blueprint, request, jsonify
from api.core.services import items as items_service
from api.core.utils.logger import get_logger
from api.core.utils.validation import validate_payload

logger = get_logger()
bp = Blueprint("items", __name__)

@bp.route("/", methods=["GET"])
def get_items():
    db = request.args.get("db")
    return jsonify(items_service.get_all_items(db))

@bp.route("/<int:item_id>", methods=["GET"])
def get_item(item_id):
    db = request.args.get("db")
    item = items_service.get_item_by_id(db, item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

@bp.route("/", methods=["POST"])
def create_item():
    db = request.args.get("db")
    payload = request.json
    try:
        validate_payload(["name", "owner_id"], payload)
        return jsonify(items_service.create_item(db, payload))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    db = request.args.get("db")
    payload = request.json
    return jsonify(items_service.update_item(db, item_id, payload))

@bp.route("/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    db = request.args.get("db")
    return jsonify(items_service.delete_item(db, item_id))
