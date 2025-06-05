"""
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
        #     1.1获取预期结果
        self.dic = eval(dic["expect"])
        #     1.2获取返回的实际结果
        self.res = res.json()
        #     1.3先断言接口的状态码
        self.status = res.status_code
        print(f"预期结果{self.dic}")
        print(f"实际结果{self.res}")
        print(f"状态码{self.status}")

# 2.定义一个对外的断言方法
    def public_assert(self):
        assert self.status in [200,304,201],f"请求失败:{self.status}"
        msg = ""
        #     1.2 循环断言字典里面的键值对
        for k,v in self.dic.items():
            print(f"解包结果1{k}:{v}")
            real = jsonpath(self.res,f"$..{k}")
            if real == False:
                # raise AssertionError(f"在相应结果内未找到")
                msg += f"\n在相应结果内，未找到预期结果字段：{k}"
            else:
                if str(v) != str(real[0]):
                    msg += f"\n断言失败：预期结果{v},与实际结果：{real[0]}不一致"
            #     1.1 断言状态码是否正确
            assert msg == "",msg

if __name__ == '__main__':
    from common.readData import ReadData
    rd = ReadData()
    testdata = rd.read_excel()
    print(f"预期结果{testdata[1]}")
    print(testdata[0]["expect"])
    from common.config_http import ConfigHttp
    chttp = ConfigHttp(testdata[1])
    res = chttp.run()
    print(f"实际结果{res.json()}")
    p = PublicAssert(testdata[1],res)
    p.public_assert()




