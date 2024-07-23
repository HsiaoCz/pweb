# 返回json给前端
from flask import Flask
from flask import json
from flask import make_response
from flask import jsonify

app = Flask(__name__)
# close json config
app.config["JSON_AS_ASCII"] = False


# return json to frontstack
@app.route("/user")
def user():
    data = {"name": "zhangsan", "age": 13}
    response = make_response(json.dump(data, ensure_ascii=False))
    response.mimetype = "application/json"
    return response


# jsonify
app.route("/hello")


def hello():
    person = {"name": "jame", "age": 12}
    return jsonify(person)


if __name__ == "__main__":
    app.run(debug=True)
