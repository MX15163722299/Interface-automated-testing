import pytest
import requests
from common.readData import ReadData
from common.pre_solve import PreSolve
from common.config_http import ConfigHttp
from common.publicAssert import PublicAssert

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
# print(test_data)
class TestCase:
    @pytest.mark.parametrize("dic",test_data)
    def test_case(self,dic):

       # 实例化依赖处理器
       ps = PreSolve(test_data)

       # 替换依赖字段，会自动执行依赖接口，并更新 dic["value"] 和 dic["header"]
       ps.preSolve(dic)

       # 实例化请求类
       ch = ConfigHttp(dic)
       response = ch.run()

       print(f"✅ 执行结果：{response}")

       # 断言
       pA = PublicAssert(dic, response)
       pA.public_assert()

if __name__ == '__main__':
    pytest.main(["-vs"])

