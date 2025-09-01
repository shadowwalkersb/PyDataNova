from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_service.routes.users_mock import bp as users_mock_bp
from flask_service.routes.items_mock import bp as items_mock_bp
from flask_service.routes.users import bp as users_bp
from flask_service.routes.items import bp as items_bp
# from routes.users import bp as users_bp
from routes.items import bp as items_bp

app = Flask(__name__)

CORS(app, origins=[
    "https://shadowwalkersb.github.io",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
], supports_credentials=True)

app.register_blueprint(users_mock_bp, url_prefix="/users-mock")
app.register_blueprint(items_mock_bp, url_prefix="/items-mock")
app.register_blueprint(users_bp, url_prefix="/users")
# Register blueprints
# app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(items_bp, url_prefix="/items")

@app.route("/")
def index():
    return {"message": "PyDataNova Flask Service running..."}

# Analytics endpoint
@app.route("/analytics/summary")
def analytics_summary():
    summary = {
        "users": 123,
        "events": 456,
        "sales": 789
    }
    return jsonify(summary)

# ML predict endpoint
@app.route("/ml/predict", methods=["POST", "GET"])
def ml_predict():
    if request.method == "GET":
        input_text = request.args.get("inputText", "default")
    else:
        input_text = request.json.get("inputText", "default")

    prediction = "cat" if "cat" in input_text.lower() else "other"
    confidence = 0.95 if prediction == "cat" else 0.67

    return jsonify({
        "input": input_text,
        "prediction": prediction,
        "confidence": confidence
    })

# RPC-style echo endpoint
@app.route("/rpc/echo", methods=["POST", "GET"])
def rpc_echo():
    if request.method == "GET":
        msg = request.args.get("msg", "hello")
    else:
        data = request.get_json() or {}
        msg = data.get("msg", "hello")
    return jsonify({"echo": msg})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
