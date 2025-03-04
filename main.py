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
import pytest
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