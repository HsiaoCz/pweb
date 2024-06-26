from requests.exceptions import HTTPError
import requests


# GET requests
requests.get("https://www.baidu.com")

# request response
response = requests.get("www.baidu.com")

# request.get()的返回值是Response的实例
# 将其存储在response的变量中

# 状态码
# 从response中获取信息之状态码
print(response.status_code)

# response status code
if response.status_code == 200:
    print("success")
elif response.status_code == 404:
    print("failed")

# requests简化了这些判断，如果response返回的状态码介于200和400之间则将计算为True
# 否则为false

# if response:
#    print("success")
# else:
#    print("an error has occurred")
# 需要注意的是，这个方法不会验证状态码是否等于200
# 原因是200到400范围内的其他状态代码，例如204 NO CONTENT和304 NOT MODIFIED
# 如果不想再if语句中检查响应的状态码，如果请求不成功，你希望抛出一个异常
# 可以使用.raise_for_status()执行操作

for url in ["https://api.github.com", "https://api.github.com/invalid"]:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred:{http_err}")
    except Exception as err:
        print(f"Other error occurred:{err}")
    else:
        print("success")
