from flask import Blueprint, jsonify, request
from core.db.neon import flask_engine
import pandas as pd
from sqlalchemy import text

bp = Blueprint("users", __name__)

@bp.route("/", methods=["GET"])
def get_users():
    query = "SELECT * FROM users;"
    try:
        with flask_engine.connect() as conn:
            df = pd.read_sql(text(query), conn)
        return df.to_dict(orient="records")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/", methods=["POST"])
def add_user():
    data = request.get_json()
    first = data.get("first")
    last = data.get("last")

    if not first or not last:
        return jsonify({"error": "Missing first or last"}), 400

    query = """
    INSERT INTO users (first, last)
    VALUES (:first, :last)
    RETURNING id, first, last;
    """
    try:
        with flask_engine.begin() as conn:
            result = conn.execute(text(query), {"first": first, "last": last})
            new_user = result.fetchone()
        return dict(new_user._mapping)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
