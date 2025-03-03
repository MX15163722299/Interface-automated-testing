
"""
1.获取数据
2.进行请求

"""
import requests
#定义一个类
class ConfigHttp(object):
    def __init__(self,dic):
        self.dic = dic
    def run(self):
        interfaceUrl = self.dic["interfaceUrl"]
        value = self.dic["value"]
        method = self.dic["method"]
        expect = self.dic["expect"]
        print(interfaceUrl, method, value, expect)
        if method == "get":
            response = self.__get()
            return response
        elif method == "post":
            response = self.__post()
            return response

    def __get(self):
        response = requests.get(self.dic["interfaceUrl"], params=eval(self.dic["value"]))
        return response
    def __post(self):
        response = requests.post(self.dic["interfaceUrl"], data=eval(self.dic["value"]))
        return response
if __name__ == '__main__':
    #测试数据
    data1 = {'id': '1', 'title': '登录成功', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'content-type': 'data', 'method': 'post', 'file_var': '', 'file_path': '', 'value': "{'username':'liangchao','password':'123456'}", 'header': '{}', 'rely': 'n', 'caseid': '', 'expect': "{'errorCode':'0','username':'liangchao'}", 'extract': '[{\'username\':\'$..username\'},{\'header\':{\'Set-Cookie\':"\'Set-Cookie\': \'(.*?)\'"}}]'}
    ch = ConfigHttp(data1)
    res = ch.run()
    print(res.text)