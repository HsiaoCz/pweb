from flask import Flask

app = Flask(__name__)

# dynamic router


@app.route("/user/<id>")
def getID(id):
    if id == 1:
        return "hello"
    if id == 2:
        return "jojo"
    if id == 3:
        return "flask"
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)
    
    
