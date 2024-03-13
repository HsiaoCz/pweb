from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/index")
def index():
    abort(404)


# 出现404错误的时候 调用
@app.errorhandler(404)
def handle_404_error(err):
    return "handle 404" + err


if __name__ == "__main__":
    app.run(debug=True)
