"""

执行测试用例
将临时报告生成为 html 的报告
发送报告文件
清理报告

"""

import os
import time
import pytest
import shutil
import subprocess  #pytest运行器
from common.log import logger
from common.send_email import SendEmail
# 修改标题
from common.allure_revise import AllureRevise


if __name__ == '__main__':
    #执行测试用例，执行测试用例生成测试报告==========================================
    #获取当前的时间
    time_local = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    logger.info(f"启动测试，当前时间：{time_local}")
    #设置报告的存放路径
    report_path = os.path.join(os.path.dirname(__file__),"testreport",time_local)
    logger.info(f"报告将保存到：{report_path}")
    #文件获取路径
    path = os.path.join(os.path.dirname(__file__), "testreport", "temp")
    logger.info(f"临时报告路径：{path}")
    #执行测试用例生成测试报告
    pytest.main(["-vs","-m","smoke",f"--alluredir={path}","--clean-alluredir"])
    logger.info("pytest 执行完毕")
    # 确保报告路径存在，如果不存在则创建
    if not os.path.exists(report_path):
        os.makedirs(report_path)
        logger.info(f"报告路径不存在，创建报告路径:{report_path}")

    #生成 Html 测试报告 ===============================================================
    #执行 Allure 报告生成命令的批处理文件
    allure_path = r"D:\Program Files\allure-2.17.3\bin\allure.bat"  #windows 的执行文件

    # allure_path = "/usr/local/bin/allure"#linux上执行文件，需要找到linux 的 allure的安装路径

    try:
        #执行 Allure 报告生成
        subprocess.run([allure_path, "generate", path, "-o", report_path], check=True)
        logger.info("Allure 报告生成成功")
    except subprocess.CalledProcessError:
        #报告生成失败
        logger.error("Allure 报告生成失败")
        raise RuntimeError("Allure 报告生成失败，请检查 allure 是否已安装并配置 PATH")
    #修改报告标题======================================================================
    index_file = os.path.join(report_path, "index.html")
    logger.info(f"报告文件路径：{index_file}")
    #判断 index.html 文件是否存在，os.path.exists() 是 Python 的标准函数，用来检查某个路径（文件或文件夹）是否真实存在。
    if not os.path.exists(index_file):
        raise FileNotFoundError(f"未找到报告文件: {index_file}")

    AllureRevise.set_windows_title("嘿嘿科技",report_path)
    #修改报告类的标题
    AllureRevise.config_title("登录模块",report_path)
    #手动创建一个脚本用于查看报告============================================================

    with open(f"{report_path}/查看报告.bat","w",encoding="utf-8") as f:
        f.write(r"allure open ./")
    #将生成的报告压缩成为zip ===============================================================
    shutil.make_archive(base_name=f"{path}/测试报告{time_local}",format="zip",root_dir=report_path)
    #使用邮箱发送报告===============================================================================
    sm = SendEmail()
    sm.send(f"{path}/测试报告{time_local}.zip")
    print("test")
    logger.info("压缩并发送报告完成")
    #钉钉通知========================================================================================
    from common.ding_talk import DingTalk
    dt = DingTalk()
    dt.send_msg('test：孟旭-接口测试报告已发邮箱')
    logger.info("钉钉通知完成")
    #自动清理报告和日志文件==========================================================================
    from common.auto_clear import autoClear,  clear_logs_keep_n
    autoClear(5, "testreport")
    clear_logs_keep_n(10, "testlog")