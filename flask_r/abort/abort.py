# abort 函数
# 在网页中主动抛出异常
from flask import Flask
from flask import abort
from flask import request
from flask import make_response


app = Flask(__name__)


@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method.get("GET"):
        return make_response("index.html")
    if request.method.get("POST"):
        name = request.form.get("name")
        password = request.form.get("password")
        if name == "zhangsan" and password == "123":
            return "login success"
        else:
            abort(404)


if __name__ == "__main__":
    app.run(debug=True)
