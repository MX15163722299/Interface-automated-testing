import allure
import pytest
from common.read_data import ReadData
from common.pre_solve import PreSolve
from common.config_http import ConfigHttp
from common.public_assert import PublicAssert

'''
导包
1.获取测试数据
2.定义一个测试类
    2.1 创建测试用例方法
        2.1.1 获取测试数据内进行请求时需要的关键字段
        2.1.2 进行请求，获取返回结果
        2.1.3 断言返回实际结果，并且判断执行成功/失败
'''

#====================================excel=========================
rd = ReadData()
#  获取测试数据 ----- 依赖模块必传必用的数据
# test_data = rd.read_excel()
#
# #获取获取订单接口数据
# test_data_get_orders = rd.read_excel_by_name("get_orders")
# #获取提交订单接口数据
# test_data_submit_order = rd.read_excel_by_name("submit_order")

#=============================yaml=========================
test_data = rd.read_yaml()

test_data_get_orders= rd.read_yaml_by_name("get_orders")
test_data_submit_order= rd.read_yaml_by_name("submit_order")



#订单模块
class  TestOrder:
    #  五、测试获取订单接口
    @pytest.mark.smoke
    # @pytest.mark.run(order=1)
    @allure.title("{dic[title]}")
    @pytest.mark.parametrize("dic", test_data_get_orders)
    def test_case_get_orders(self, dic, db):
        # 实例化依赖处理器
        ps = PreSolve(test_data)
        # 替换依赖字段，会自动执行依赖接口，并更新 dic["value"] 和 dic["header"]
        ps.preSolve(dic)
        # 实例化请求类
        ch = ConfigHttp(dic)
        response = ch.run()
        print(f"执行结果：{response}")
        # 断言
        pA = PublicAssert(dic, response, db)
        pA.public_assert()

    #  六、测试提交订单接口
    @pytest.mark.smoke
    # @pytest.mark.run(order=1)
    @allure.title("{dic[title]}")
    @pytest.mark.parametrize("dic", test_data_submit_order)
    def test_case_submit_order(self, dic, db):
        # 实例化依赖处理器
        ps = PreSolve(test_data)
        # 替换依赖字段，会自动执行依赖接口，并更新 dic["value"] 和 dic["header"]
        ps.preSolve(dic)
        # 实例化请求类
        ch = ConfigHttp(dic)
        response = ch.run()
        print(f"执行结果：{response}")
        # 断言
        pA = PublicAssert(dic, response, db)
        pA.public_assert()


if __name__ == '__main__':
    pytest.main(["-s", "test_order_api.py"])