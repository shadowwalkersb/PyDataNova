from flask import Blueprint, request, jsonify
from core.db.neon import engine
from sqlalchemy import text

bp = Blueprint("users", __name__)

@bp.route("/", methods=["GET"])
def get_users():
    conn = engine.connect()
    res = conn.execute(text("SELECT * FROM users"))
    # conn.execute(text("insert into users (first, last) values ('Jane','Doe')"))
    # conn.commit()
    return [{"id": row[0], "first": row[1], "last": row[2]} for row in res]

@bp.route("/", methods=["POST"])
def add_user():
    data = request.get_json()
    first = data.get("first")
    last = data.get("last")
    if not first or not last:
        return jsonify({"error": "Missing first or last name"}), 400

    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO users (first, last) VALUES (:first, :last)"),
            {"first": first, "last": last}
        )
        conn.commit()
    return jsonify({"status": "ok"}), 201
