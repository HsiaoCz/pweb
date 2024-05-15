from flask import Flask

# __name__ current file
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)
