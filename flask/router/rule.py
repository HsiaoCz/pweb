from flask import Flask

app = Flask(__name__)

# dynamic router


@app.route("/user/<id>")
def getId(id):
    if id == 1:
        return "Hello"
    if id == 2:
        return "jojo"
    if id == 3:
        return "flask"
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
