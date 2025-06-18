
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
            response = self.__post_form()
            return response
        elif self.method == "post" and self.contentType == "json":
            response = self.__post_json()
            return response
    def __get(self):
        # response = requests.get(self.dic["interfaceUrl"], params=eval(self.dic["value"]),headers=eval(self.dic["header"]))
        # return response
        try:
            url = self.dic["interfaceUrl"]
            # value 和 header 可能是 str 或 dict
            value = self.dic["value"]
            if isinstance(value, str):
                value = eval(value)
            header = self.dic["header"]
            if isinstance(header, str):
                header = eval(header)
            response = requests.get(url, params=value, headers=header)
            return response
        except Exception as e:
            print("请求失败！")
            print(f"URL: {self.dic.get('interfaceUrl')}")
            print(f"Value: {self.dic.get('value')}")
            print(f"Header: {self.dic.get('header')}")
            print(f"错误详情: {repr(e)}")
            return None

    def __post_form(self):
       # response = requests.post(self.dic["interfaceUrl"], data=eval(self.dic["value"]),headers=eval(self.dic["header"]))
       # return response
       try:
           url = self.dic["interfaceUrl"]
           # value 和 header 可能是 str 或 dict
           value = self.dic["value"]
           if isinstance(value, str):
               value = eval(value)
           header = self.dic["header"]
           if isinstance(header, str):
               header = eval(header)
           response = requests.post(url, data=value, headers=header)
           return response

       except Exception as e:
           print("请求失败！")
           print(f"URL: {self.dic.get('interfaceUrl')}")
           print(f"Value: {self.dic.get('value')}")
           print(f"Header: {self.dic.get('header')}")
           print(f"错误详情: {repr(e)}")
           return None
    def __post_json(self):
        # response = requests.post(self.dic["interfaceUrl"], json=eval(self.dic["value"]),headers=eval(self.dic["header"]))
        # return response
        try:
            url = self.dic["interfaceUrl"]
            # value 和 header 可能是 str 或 dict
            value = self.dic["value"]
            if isinstance(value, str):
                value = eval(value)
            header = self.dic["header"]
            if isinstance(header, str):
                header = eval(header)
            response = requests.post(url, json=value, headers=header)
            return response

        except Exception as e:
            print("请求失败！")
            print(f"URL: {self.dic.get('interfaceUrl')}")
            print(f"Value: {self.dic.get('value')}")
            print(f"Header: {self.dic.get('header')}")
            print(f"错误详情: {repr(e)}")
            return None
if __name__ == '__main__':
    #测试数据
    # data1 = {'id': 2.0, 'title': '用户登录', 'interfaceUrl': 'http://localhost:5000/login', 'name': 'login', 'contentType': 'form', 'method': 'post', 'file_var': '', 'file_path': '', 'value': "{'username': 'user1', 'password': 'p001'}", 'header': '{}', 'rely': 'n', 'caseid': '', 'expect': "{'errorCode': 0}", 'extract': "[{'Set-Cookie': 'uid'}]"}
    from common.read_data import ReadData
    r = ReadData()
    # data = r.read_excel()
    # ch = ConfigHttp(data[3])
    # res = ch.run()
    # print(res.text)


    # j = r.read_json()
    y = r.read_yaml()
    print(y[2])
    from common.pre_solve import PreSolve
    ps = PreSolve(y)
    # 替换依赖字段，会自动执行依赖接口，并更新 dic["value"] 和 dic["header"]
    ps.preSolve(y[6])
    print(f"==========={y[6]}")
    ch = ConfigHttp(y[6])
    res = ch.run()
    print(f"结果:{res.text}")