from flask import Flask
from types import User

# router

app = Flask(__name__)


@app.route("/user/register", methods=["POST"], endpoint="hello")
def register():
    return "注册成功"


# endpoint 假如两个路由使用了相同的函数
# 需要使用endpoint来指定端点
@app.route("/hi", methods=["POST", "GET"], endpoint="hi")
def hi():
    return "hi"


if __name__ == "__main__":
    app.run(debug=True)
