
"""
1.获取数据
2.进行请求
"""
from http.client import responses

import requests
#定义一个类
class ConfigHttp(object):
    def __init__(self,dic):
        self.dic = dic
        self.interfaceUrl = dic["interfaceUrl"]
        self.method = dic["method"]
        self.value = dic["value"]
        self.expect = dic["expect"]
        self.contentType = dic["contentType"]

    def run(self):
        print(self.interfaceUrl, self.method, self.value, self.expect, self.contentType)
        if self.method == "get":
            response = self.__get()
            return response
        elif self.method == "post" and self.contentType == "form":
            response = self.__post_from()
            return response
        elif self.method == "post" and self.contentType == "json":
            response = self.__post_json()
            return response

    def __get(self):
        response = requests.get(self.dic["interfaceUrl"], params=eval(self.dic["value"]),headers=eval(self.dic["header"]))
        return response
    def __post_from(self):
        response = requests.post(self.dic["interfaceUrl"], data=eval(self.dic["value"]),headers=eval(self.dic["header"]))
        return response
    def __post_json(self):
        response = requests.post(self.dic["interfaceUrl"], json=eval(self.dic["value"]),headers=eval(self.dic["header"]))
        return response
if __name__ == '__main__':
    #测试数据
    # data1 = {'id': 2.0, 'title': '用户登录', 'interfaceUrl': 'http://localhost:5000/login', 'name': 'login', 'contentType': 'form', 'method': 'post', 'file_var': '', 'file_path': '', 'value': "{'username': 'user1', 'password': 'p001'}", 'header': '{}', 'rely': 'n', 'caseid': '', 'expect': "{'errorCode': 0}", 'extract': "[{'Set-Cookie': 'uid'}]"}
    from common.readData import ReadData
    r = ReadData()
    # data = r.read_excel()
    # j = r.read_json()
    y = r.read_yaml()
    ch = ConfigHttp(y[1])
    res = ch.run()
    print(res.text)