from flask import Blueprint, jsonify, request
from core.db.neon import flask_engine
import pandas as pd
from sqlalchemy import text

bp = Blueprint("items", __name__)

@bp.route("/", methods=["GET"])
def get_items():
    query = "SELECT * FROM items;"
    try:
        with flask_engine.connect() as conn:
            df = pd.read_sql(text(query), conn)
        return df.to_dict(orient="records")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/", methods=["POST"])
def add_item():
    data = request.get_json()
    name = data.get("name")
    category = data.get("category")
    price = data.get("price")
    owner_id = data.get("owner_id")

    if not name or not category or not price or not owner_id:
        return jsonify({"error": "Missing name or category or price or owner_id"}), 400

    query = """
    INSERT INTO items (name, category, price, owner_id)
    VALUES (:name, :category, :price, :owner_id)
    RETURNING id, name, category, price, owner_id;
    """
    try:
        with flask_engine.begin() as conn:
            result = conn.execute(text(query), {"name": name, "category": category, "price": price, "owner_id": owner_id})
            new_user = result.fetchone()
        return dict(new_user._mapping)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
