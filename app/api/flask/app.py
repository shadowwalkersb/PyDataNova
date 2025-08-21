from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"message": "PyDataNova Flask v6 running"}
