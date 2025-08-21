from flask import Flask
from routes import users, items

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(users.bp, url_prefix="/users")
app.register_blueprint(items.bp, url_prefix="/items")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
