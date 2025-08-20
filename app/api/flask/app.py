from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow cross-origin requests

@app.route("/root")
def root():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/mock-data")
def mock_data():
    return jsonify({"data": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
