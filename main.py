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
from common.conf_test import db

if __name__ == '__main__':
    #获取当前的时间
    time_local = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    logger.info(f"启动测试，当前时间：{time_local}")
    #设置报告的存放路径
    report_path = os.path.join(os.path.dirname(__file__),"testReport",time_local)
    logger.info(f"报告将保存到：{report_path}")

    #文件获取路径

    path = os.path.join(os.path.dirname(__file__), "testReport", "temp")

    logger.info(f"临时报告路径：{path}")
    #执行测试用例生成测试报告

    pytest.main(["-vs",f"--alluredir={path}","--clean-alluredir"])
    logger.info("pytest 执行完毕")
    # 确保报告路径存在，如果不存在则创建
    if not os.path.exists(report_path):
        os.makedirs(report_path)

    #将临时报告转化为真正的

    import subprocess

    allure_path = r"D:\Program Files\allure-2.17.3\bin\allure.bat"

    try:
        subprocess.run([allure_path, "generate", path, "-o", report_path], check=True)
        logger.info("Allure 报告生成成功")
    except subprocess.CalledProcessError:
        logger.error("Allure 报告生成失败")
        raise RuntimeError("Allure 报告生成失败，请检查 allure 是否已安装并配置 PATH")

    index_file = os.path.join(report_path, "index.html")
    if not os.path.exists(index_file):
        raise FileNotFoundError(f"未找到报告文件: {index_file}")

    #修改标题
    from common.allure_revise import AllureRevise

    AllureRevise.set_windows_title("嘿嘿科技",report_path)
    #修改报告类的标题
    AllureRevise.config_title("登录模块",report_path)
    #手动创建一个脚本用于查看报告

    with open(f"{report_path}/查看报告.bat","w",encoding="utf-8") as f:
        f.write(r"allure open ./")
    #将生成的报告压缩成为zip
    shutil.make_archive(base_name=f"{path}/测试报告{time_local}",format="zip",root_dir=report_path)

    sm = SendEmail()
    sm.send(f"{path}/测试报告{time_local}.zip")
    print("test")
    logger.info("压缩并发送报告完成")
    from common.ding_talk import DingTalk
    dt = DingTalk()
    dt.send_msg('test：孟旭-接口测试报告已发邮箱')
    logger.info("钉钉通知完成")

    from common.auto_clear import autoClear,  clear_logs_keep_n
    autoClear(5, "testReport")
    clear_logs_keep_n(10, "testLog")