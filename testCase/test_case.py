
import pytest
from common.readData import ReadData
import requests
from common.configHttp import ConfigHttp
from common.publicAssert import PublicAssert
from common.pre_solve import PreSolve
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

        #实例化，解决依赖
        ps = PreSolve(test_data)
        #替换依赖值header,value
        dic["header"],dic["value"] = ps.preSolve(dic)
       #实例化公共请求类
        ch = ConfigHttp(dic)
       #调用请求方法
        response = ch.run()
        print(f"结果：========={response}")
        # assert str(res_dict["errorCode"]) == str(eval(dic["expect"])["errorCode"]),"预期结果与实际结果不符合"
        # try:
        #     assert str(res_dict["errorCode"]) == str(eval(dic["expect"])["errorCode"]),"预期结果与实际结果不符合"
        # except Exception as e:
        #     print(f"\n用例执行失败")
        #     raise


       # 实例化断言
        pA = PublicAssert(dic,response)
        pA.public_assert()

if __name__ == '__main__':
    pytest.main(["-vs"])
#
# import pytest
# list1 = [1, 2, 3,4,5]
# list2 = [[1,2],[2,2],[2,3],[2,4],[2,5]]
# class TestClass:
#     # @pytest.mark.parametrize("args",list1)
#     # def test_case(self,args):
#     #     print(f"\n执行测试用例的数据{args}")
#     #     assert args == 5,"这个数不是5"
#     @pytest.mark.parametrize("num1,num2",list2)
#     def test_case2(self,num1,num2):
#         print(f"\n执行测试用例的参数{num1}/{num2}")
#         assert num1 == num2,"两个数不相等"
# if __name__ == '__main__':
#     pytest.main(["-vs"])
