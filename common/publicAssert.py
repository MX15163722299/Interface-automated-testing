"""
{'errorCode':'0','username':'liangchao'}

定义一一个类

1.定义初始化方法：
    1.1获取预期结果
    1.2获取返回的实际结果
    1.3先断言接口的状态码

2.定义一个对外的断言方法
    1.1 断言状态码是否正确
    1.2 循环断言字典里面的键值对


"""
from jsonpath import jsonpath


class PublicAssert:
# 1.定义初始化方法：
    def __init__(self,dic,res):
        self.dic = eval(dic["expect"])
        self.res = res.json()
        self.status = res.status_code
        print(f"预期结果{self.dic}")
        print(f"实际结果{self.res}")
        print(f"状态码{self.status}")
#     1.1获取预期结果
#     1.2获取返回的实际结果
#     1.3先断言接口的状态码
#
# 2.定义一个对外的断言方法
    def public_assert(self):
        assert self.status in [200,304],f"请求失败:{self.status}"

        for k,v in self.dic.items():
            print(f"解包结果{k}:{v}")
            real = jsonpath(self.res,"$.." + k)
            if real == False:
                raise AssertionError(f"在相应结果内未找到")
            else:
                real = real[0]
            assert str(real) == str(v),f"预期{v},实际结果{real},不相符"
#     1.1 断言状态码是否正确
#     1.2 循环断言字典里面的键值对

if __name__ == '__main__':
    from common.readData import ReadData
    rd = ReadData()
    testdata = rd.read_excel()
    # print(f"预期结果{testdata[0]}")
    # print(testdata[0]["expect"])
    from common.configHttp import ConfigHttp
    chttp = ConfigHttp(testdata[0])

    res = chttp.run()
    # print(f"实际结果{res.json()}")
    p = PublicAssert(testdata[0],res)
    p.public_assert()
    # a = {'data': {'admin': False, 'chapterTops': [], 'coinCount': 82928, 'collectIds': [12489, 12554, 20867, 20535, 20932, 20931, 20925, 20923, 21681, 1165, 2334, -1, 23168, 23646, 24990, 25477, 26578, 26503, 26583, 12240, 24206, 26795, -1, -1, 18615, -1, 21498, 8652, 26624, 28069, 27996, 18281, 8857, -1], 'email': 'rainshine1190@126.com', 'icon': '', 'id': 17180, 'nickname': 'liangchao', 'password': '', 'publicName': 'liangchao', 'token': '', 'type': 0, 'username': 'liangchao'}, 'errorCode': 0, 'errorMsg': ''}
    # data = {"name":"tom","mag":{"age":10,"name":"汤姆"}}
    #
    # b = jsonpath(data,"$..name")
    # b = jsonpath(data,"$.name")
    # print(b)   