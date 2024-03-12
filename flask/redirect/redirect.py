# 重定向
from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "hello"


# 1. 重定向的第一种方式
# 重定向到url
@app.route("/redirect")
def direct():
    return redirect("https://www.baidu.com")


# 2 url_for
# 重定向到自己的代码当中
@app.route("/url")
def urlh():
    return redirect(url_for("hello"))


if __name__ == "__main__":
    app.run(debug=True)
