"""

执行测试用例


将临时报告生成为 html 的报告


发送报告文件


清理报告


"""
import os
import time

import pytest

if __name__ == '__main__':
    #设置报告的存放路径
    report_path =  os.path.dirname(__file__)+"/testReport/report"
    path = os.path.dirname(__file__)+"/testReport/temp"
    print(report_path)

    #执行测试用例生成测试报告

    pytest.main(["-vs","--alluredir="+path,"--clean-alluredir"])
    time.sleep(3)
    #将临时报告转化为真正的
    os.system(f"allure generate {path} -o {report_path}")