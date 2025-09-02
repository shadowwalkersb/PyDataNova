from flask import Blueprint, jsonify
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
