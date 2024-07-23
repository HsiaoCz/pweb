from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/index")
def index():
    data = {
        "name": "zhangsan",
        "age": 18,
    }
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
