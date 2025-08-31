from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_service.routes.users_mock import bp as users_mock_bp
from flask_service.routes.items_mock import bp as items_mock_bp
from flask_service.routes.users import bp as users_bp
from flask_service.routes.items import bp as items_bp
import random
from datetime import datetime

app = Flask(__name__)


CORS(app, origins=[
    "https://shadowwalkersb.github.io",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
], supports_credentials=True)

app.register_blueprint(users_mock_bp, url_prefix="/users-mock")
app.register_blueprint(items_mock_bp, url_prefix="/items-mock")
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(items_bp, url_prefix="/items")

@app.route("/")
def index():
    return {"message": "PyDataNova Flask Service running..."}

# ----------------------
# Analytics Endpoints
# ----------------------
@app.route("/analytics/summary")
def analytics_summary():
    return jsonify({"mean": 42.0, "std": 3.14, "count": 100})

@app.route("/analytics/top-n")
def analytics_top_n():
    data = [{"item": f"item{i}", "value": i*10} for i in range(1, 6)]
    return jsonify(data)

@app.route("/analytics/stats")
def analytics_stats():
    return jsonify({"min": 1, "max": 100, "median": 50, "percentiles": {"25": 25, "75": 75}})

@app.route("/analytics/trends")
def analytics_trends():
    timeseries = [{"date": f"2025-08-{i:02d}", "value": random.randint(10, 100)} for i in range(1, 8)]
    return jsonify(timeseries)

# ----------------------
# ML Endpoints
# ----------------------
@app.route("/ml/predict", methods=["GET", "POST"])
def ml_predict():
    input_text = ""
    if request.method == "GET":
        input_text = request.args.get("inputText", "default")
    else:
        data = request.get_json() or {}
        input_text = data.get("inputText", "default")
    return jsonify({"input": input_text, "prediction": "cat", "confidence": 0.95})

@app.route("/ml/info")
def ml_info():
    return jsonify({"model": "DummyClassifier", "version": "1.0"})

# ----------------------
# RPC-style endpoints
# ----------------------
@app.route("/rpc/echo", methods=["GET", "POST"])
def rpc_echo():
    data = request.get_json() or {"message": "hello"}
    return jsonify(data)

@app.route("/rpc/time")
def rpc_time():
    return jsonify({"server_time": datetime.utcnow().isoformat()})

@app.route("/rpc/math/add", methods=["POST"])
def rpc_add():
    data = request.get_json() or {}
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"result": a + b})

@app.route("/rpc/random")
def rpc_random():
    return jsonify({"value": random.random()})

# ----------------------
# Image Endpoints
# ----------------------
@app.route("/image/face-detect")
def face_detect():
    return jsonify({"faces_detected": 2})

@app.route("/image/enhance")
def enhance():
    return jsonify({"status": "success", "message": "image enhanced"})

@app.route("/image/resize")
def resize():
    return jsonify({"status": "success", "message": "image resized"})

@app.route("/image/filter")
def image_filter():
    return jsonify({"status": "success", "message": "filter applied"})

# ----------------------
# User / Item Endpoints (demo)
# ----------------------
@app.route("/users/list")
def users_list():
    users = [{"id": i, "name": f"User{i}"} for i in range(1, 6)]
    return jsonify(users)

@app.route("/users/<int:user_id>")
def users_get(user_id):
    return jsonify({"id": user_id, "name": f"User{user_id}"})

@app.route("/items/list")
def items_list():
    items = [{"id": i, "name": f"Item{i}"} for i in range(1, 6)]
    return jsonify(items)

@app.route("/items/<int:item_id>")
def items_get(item_id):
    return jsonify({"id": item_id, "name": f"Item{item_id}"})

# ----------------------
# Search / Misc Endpoints
# ----------------------
@app.route("/search")
def search():
    q = request.args.get("q", "")
    return jsonify({"query": q, "results": [f"{q}_1", f"{q}_2", f"{q}_3"]})

@app.route("/health")
def health():
    return jsonify({"status": "ok", "uptime": "12345s"})

@app.route("/version")
def version():
    return jsonify({"app": "PyDataNova Flask", "version": "v1.0"})

# ----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
