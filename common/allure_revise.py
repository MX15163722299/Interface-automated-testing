import json
class AllureRevise():
    @staticmethod
    def set_windows_title(new_title,file_path):
        with open(f"{file_path}/index.html",'r+',encoding='utf-8') as f:
            all_lines = f.readlines()
        with open(f"{file_path}/index.html",'w',encoding='utf-8') as w:
            for line in all_lines:
                w.write(line.replace("Allure Report",new_title))

    #修改报告内的标题：config_title
    @staticmethod
    def config_title(name,file_path):
        file_path = f"{file_path}/widgets/summary.json"
        with open(file_path,'rb') as f:
            #json文件流解析成python字典
            param = json.load(f)
            param["reportName"] = name
        with open(file_path,'w',encoding='utf-8') as w:
            #将python字典数据写入json
            json.dump(param,w,ensure_ascii=False,indent=4)
