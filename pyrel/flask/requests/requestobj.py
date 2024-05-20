# request 包含前端发送过来的所有请求

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return "Hello"


@app.route("/index", methods=["POST"])
def index():
    if request.method == "POST":
        return request.remote_addr


@app.route("/user", methods=["POST"])
def user():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username, password)
    return "ok"
