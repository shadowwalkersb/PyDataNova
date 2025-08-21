from flask import Flask
from flask_cors import CORS
from routes.users import bp as users_bp
from routes.items import bp as items_bp

app = Flask(__name__)

CORS(app, origins=["http://localhost:5500",
                   "http://127.0.0.1:5500",
                   ])  # allow your frontend

app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(items_bp, url_prefix="/items")

@app.route("/")
def index():
    return {"message": "PyDataNova Flask v6 running"}
