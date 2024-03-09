from flask import Flask
from flask import render_template


# 实例化一个app
app = Flask(__name__)


@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template("template/index.html")


if __name__ == "__main__":
    app.run(debug=True)
