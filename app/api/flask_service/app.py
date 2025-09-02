from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_service.routes.users_mock import bp as users_mock_bp
from flask_service.routes.items_mock import bp as items_mock_bp
from flask_service.routes.users import bp as users_bp
from flask_service.routes.items import bp as items_bp

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

# Analytics endpoint
@app.route("/analytics/summary")
def analytics_summary():
    # Dummy summary data
    summary = {
        "mean": 42.0,
        "std": 3.14,
        "count": 100
    }
    return jsonify(summary)

# ML predict endpoint
@app.route("/ml/predict", methods=["POST", "GET"])
def ml_predict():
    # Dummy prediction
    input_text = request.args.get("inputText", "default") if request.method == "GET" else request.json.get("inputText", "default")
    result = {
        "input": input_text,
        "prediction": "cat",
        "confidence": 0.95
    }
    return jsonify(result)

# RPC-style echo endpoint
@app.route("/rpc/echo", methods=["POST", "GET"])
def rpc_echo():
    data = request.get_json() or {"message": "hello"}
    return jsonify(data)

# Image endpoints
@app.route("/image/face-detect")
def face_detect():
    return jsonify({"faces_detected": 2})

@app.route("/image/enhance")
def enhance():
    return jsonify({"status": "success", "message": "image enhanced"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
