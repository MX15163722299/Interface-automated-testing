import pytest
from common.read_data import ReadData
from common.pre_solve import PreSolve
from common.config_http import ConfigHttp
from common.public_assert import PublicAssert
import allure
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
#  获取测试数据 ----- 依赖模块必传必用的数据
test_data = rd.read_excel()
#  获取登录接口数据  --  每个测试用例的数据
test_data_login = rd.read_excel_by_name("login")
#获取注册接口数据
test_data_register = rd.read_excel_by_name("register")
#获取获取用户信息接口数据
test_data_get_user_info = rd.read_excel_by_name("get_user_info")
#获取更新用户信息接口数据
test_data_update_user_info = rd.read_excel_by_name("update_user_info")

from common.conf_test import db

#用户模块
class TestUserInfo:

    #一、测试注册接口 test_data_register
    @pytest.mark.skip(reason="注册接口暂不测试，跳过")
    @pytest.mark.smoke
    # @pytest.mark.run(order=1)
    @allure.title("{dic[title]}")
    @pytest.mark.parametrize("dic",test_data_register)
    def test_case_register(self,dic,db):
       # 实例化依赖处理器
       ps = PreSolve(test_data)
       # 替换依赖字段，会自动执行依赖接口，并更新 dic["value"] 和 dic["header"]
       ps.preSolve(dic)
       # 实例化请求类
       ch = ConfigHttp(dic)
       response = ch.run()
       print(f"✅ 执行结果：{response}")
       # 断言
       pA = PublicAssert(dic, response,db)
       pA.public_assert()

    # 二、 测试登录接口 test_data_login
    @pytest.mark.smoke
    # @pytest.mark.run(order=1)
    @allure.title("{dic[title]}")
    @pytest.mark.parametrize("dic",test_data_login)
    def test_case_login(self,dic,db):
       # 实例化依赖处理器
       ps = PreSolve(test_data)
       # 替换依赖字段，会自动执行依赖接口，并更新 dic["value"] 和 dic["header"]
       ps.preSolve(dic)
       # 实例化请求类
       ch = ConfigHttp(dic)
       response = ch.run()
       print(f"✅ 执行结果：{response}")
       # 断言
       pA = PublicAssert(dic, response,db)
       pA.public_assert()

    #  三、测试获取用户信息接口
    @pytest.mark.smoke
    # @pytest.mark.run(order=1)
    @allure.title("{dic[title]}")
    @pytest.mark.parametrize("dic",test_data_get_user_info)
    def test_case_get_user_info(self,dic,db):
       # 实例化依赖处理器
       ps = PreSolve(test_data)
       # 替换依赖字段，会自动执行依赖接口，并更新 dic["value"] 和 dic["header"]
       ps.preSolve(dic)
       # 实例化请求类
       ch = ConfigHttp(dic)
       response = ch.run()
       print(f"✅ 执行结果：{response}")
       # 断言
       pA = PublicAssert(dic, response,db)
       pA.public_assert()

    #  四、测试更新用户信息接口
    @pytest.mark.smoke
    # @pytest.mark.run(order=1)
    @allure.title("{dic[title]}")
    @pytest.mark.parametrize("dic",test_data_update_user_info)
    def test_case_update_user_info(self, dic, db):
        # 实例化依赖处理器
        ps = PreSolve(test_data)
        # 替换依赖字段，会自动执行依赖接口，并更新 dic["value"] 和 dic["header"]
        ps.preSolve(dic)
        # 实例化请求类
        ch = ConfigHttp(dic)
        response = ch.run()
        print(f"✅ 执行结果：{response}")
        # 断言
        pA = PublicAssert(dic, response, db)
        pA.public_assert()


if __name__ == '__main__':
    pytest.main(["-vs"])

