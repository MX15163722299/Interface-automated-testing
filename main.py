"""

执行测试用例
将临时报告生成为 html 的报告
发送报告文件
清理报告

"""


import os
import time
from shutil import make_archive
import pytest
import shutil
from common.send_email import SendEmail
from common.auto_clear import autoClear
from common.log import logger

if __name__ == '__main__':
    #获取当前的时间
    time_local = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    logger.info(f"info:{time_local}")
    #设置报告的存放路径
    report_path =  os.path.dirname(__file__) + f"/testReport/{time_local}"
    print(report_path)

    #文件获取路径
    path = os.path.dirname(__file__)+"/testReport/temp"

    logger.info(f"info:{path}")
    #执行测试用例生成测试报告

    pytest.main(["-vs",f"--alluredir={path}","--clean-alluredir"])

    #将临时报告转化为真正的
    os.system(f"allure generate {path} -o {report_path}")

    #修改标题
    from common.allure_revise import AllureRevise

    AllureRevise.set_windows_title("甜心科技",report_path)
    #修改报告类的标题
    AllureRevise.config_title("登录模块",report_path)
    #手动创建一个脚本用于查看报告

    with open(f"{report_path}/查看报告.bat","w",encoding="utf-8") as f:
        f.write(r"allure open ./")
    #将生成的报告压缩成为zip
    shutil.make_archive(base_name=f"{path}/测试报告{time_local}",format="zip",root_dir=report_path)

    autoClear(2)
    sm = SendEmail()
    sm.send(f"{path}/测试报告{time_local}.zip")
    print("test")
