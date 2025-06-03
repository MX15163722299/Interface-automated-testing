import requests

# 登录接口

url1 = "http://127.0.0.1:5000/login"
payload = {"username": "user1", "password": "p001"}
# 进行请求
res = requests.post(url=url1, data=payload)

print(res.text)