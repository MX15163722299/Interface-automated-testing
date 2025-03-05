"""

执行测试用例


将临时报告生成为 html 的报告


发送报告文件


清理报告


"""
# import json
# def set_windows_title(new_title,file_path):
#     with open(f"{file_path}/index.html",'r+',encoding='utf-8') as f:
#         all_lines = f.readlines()
#     with open(f"{file_path}/index.html",'w',encoding='utf-8') as w:
#         for line in all_lines:
#             w.write(line.replace("Allure Report",new_title))
#
# #修改报告内的标题：config_title
# def config_title(name,file_path):
#     file_path = f"{file_path}/widgets/summary.json"
#     with open(file_path,'rb') as f:
#         #json文件流解析成python字典
#         param = json.load(f)
#         param["reportName"] = name
#     with open(file_path,'w',encoding='utf-8') as w:
#         #将python字典数据写入json
#         json.dump(param,w,ensure_ascii=False,indent=4)


import os
import time
from shutil import make_archive

import pytest
import shutil
from common.send_email import SendEmail

#清理报告

#全部清理
    #获取报告路径下的文件夹名字
def auto_clear(n):
    dir = f"{os.path.dirname(__file__)}/testReport/"
    file_list = os.listdir(dir)
    print(file_list)
    file_list.sort(key=lambda x: os.path.getmtime(dir+x))
    print(file_list[:n])
    for file in file_list[:n]:
        shutil.rmtree(dir+file)



if __name__ == '__main__':
    #获取当前的时间
    time_local = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    print(time_local)
    #设置报告的存放路径
    report_path =  os.path.dirname(__file__) + f"/testReport/{time_local}"
    print(report_path)

    #文件获取路径
    path = os.path.dirname(__file__)+"/testReport/temp"
    print(path)

    #执行测试用例生成测试报告

    pytest.main(["-vs",f"--alluredir={path}","--clean-alluredir"])
    time.sleep(3)
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
    auto_clear(5)
    sm = SendEmail()
    sm.send(f"{path}/测试报告{time_local}.zip")
    print("test")
