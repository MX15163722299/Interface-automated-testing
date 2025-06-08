import requests
#
##=========================URL=======================================
##1.注册接口
url1 = "http://localhost:5000/register"

##2.登录接口

url2 = "http://localhost:5000/login"

# 3.获取用户信息
#
url3 = "http://localhost:5000/profile"
#
#4.查询商品信息
#
url4 = "http://localhost:5000/get_product"
#
#5.提交订单
#
url5 = "http://localhost:5000/submit_order"
#
#6.查询订单
#
url6 = "http://localhost:5000/get_orders"
#
#7.更新用户信息
#
url7 = "http://localhost:5000/update_user_info"

#====================================参数========================================

#1.注册
payload_1 = {"username": "testuser1", "password": "1234567","age":20,"sex":"male"}

#2.登录
payload_2 = {"username": "user1", "password": "p001"}

#3.获取用户信息
pass

#4.查询商品信息

payload_4 = {"productid": "product1"}

#5.提交订单

payload_5 = {"productid": "product1"}

#6.查询订单

pass

#7.更新用户信息

payload_7 = {'username': 'user1', 'info': {'age': 25}}

#更新用户信息


#================================请求=====================================

# 1.进行请求

# res = requests.post(url=url1, json=payload)

##2.登录接口

# res = requests.post(url=url2, data=payload_2)

# 3.获取用户信息

headers = {
    "Cookie": "uid=u001; Path=/"}
res = requests.get(url=url3,headers=headers)

#4.查询商品信息

# res = requests.get(url=url4, params=payload_4,headers="")

#5.提交订单

# headers = {
#     "Cookie": "uid=u001; Path=/"}
#
# res = requests.post(url=url5, headers=headers,json=payload_5)

#6.查询订单
# headers = {
#     "Cookie": "uid=u001; Path=/"}
# res = requests.get(url=url6, headers=headers)

#7.更新订单

# headers = {
#     "Cookie": "uid=u001; Path=/"}
#
# res = requests.post(url=url7, json=payload_7,headers=headers)

print(res.status_code)
# #
print(res.text)
# #
# print("返回的 Cookie：", session.cookies.get_dict())


