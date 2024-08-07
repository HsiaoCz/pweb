from flask import Flask

# __name__ current file

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello"


if __name__ == "__main__":
    app.run(debug=True)
