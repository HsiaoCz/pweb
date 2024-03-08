from flask import Flask

app = Flask(__name__)


# string 接收任何不带斜杠的文本
# int 接收正整数
# float 接收正浮点数
# path 接收包含斜杠的文本
@app.route("/user/<string:id>")
def index():
    if id == "hello":
        return "hi"


if __name__ == "__main__":
    app.run(debug=True)
