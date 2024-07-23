from typing import Any
from flask import Flask

# <> 提取参数
# <int:id> int 转换器

# 自定义转换器需要导入的包
from werkzeug.routing import BaseConverter
from werkzeug.routing.map import Map

app = Flask(__name__)


class RegexConvert(BaseConverter):
    def __init__(self, url_map, regex):
        # 调用父类方法
        super().__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        print("to_python 方法已经被调用")
        return value


# 将自定义的转换器类添加到flask应用中
app.url_map.converters["re"] = RegexConvert


@app.route("/user/<re('1\d{10}'):value>")
def hello(value):
    print(value)
    print("hello")


if __name__ == "__main__":
    app.run(debug=True)
