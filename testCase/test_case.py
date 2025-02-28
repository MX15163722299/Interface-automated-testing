
import pytest
from common.readData import ReadData
import requests
'''
导包
1.获取测试数据
2.定义一个测试类
    2.1 创建测试用例方法
        2.1.1 获取测试数据内进行请求时需要的关键字段
        2.1.2 进行请求，获取返回结果
        2.1.3 断言返回实际结果，并且判断执行成功/失败


'''

rd = ReadData()

test_data = rd.read_excel()

print(test_data)

class TestCase:
    def test_case(self):
        interfaceUrl = test_data[0]["interfaceUrl"]
        method = test_data[0]["method"]
        value = test_data[0]["value"]
        expect = test_data[0]["expect"]
        print(interfaceUrl, method, value, expect)
        if method == "get":
            response = requests.get(interfaceUrl,params=eval(value))
        elif method == "post":
            response = requests.post(interfaceUrl,data=eval(value))
        res_dict = response.json()
        # expect = expect.json()

        assert str(res_dict["errorCode"]) == str(eval(expect)["errorCode"]),"预期结果与实际结果不符合"
if __name__ == '__main__':
    pytest.main(["-vs"])

