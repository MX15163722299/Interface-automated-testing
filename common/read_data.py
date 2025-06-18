import xlrd
import os
import json
import yaml

class ReadData():
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.path_name = os.path.join(base_dir, "testdata", "data.xls")  # ← 修改为你的文件名
        print(f"📖 当前用例路径：{self.path_name}")

        self.read_book = xlrd.open_workbook(self.path_name)
        self.sheet = self.read_book.sheet_by_index(0)
        self.max_row = self.sheet.nrows
        self.max_col = self.sheet.ncols
        self.first_row = self.sheet.row_values(0)

    def read_excel(self):
        res_list = []
        for i in range(1, self.max_row):
            row_values = self.sheet.row_values(i, 0)
            # 去除字段中的前后空格
            cleaned = [str(cell).strip() if isinstance(cell, str) else cell for cell in row_values]
            # 跳过空行
            if all([v == '' for v in cleaned]):
                continue
            data_dict = dict(zip(self.first_row, cleaned))
            # 模块名归一化处理
            if "name" in data_dict:
                data_dict["name"] = data_dict["name"].strip().lower()
            res_list.append(data_dict)
        return res_list

    def read_excel_by_name(self, name_name: str):
        """按模块名筛选Excel用例，name 不区分大小写"""
        all_data = self.read_excel()
        return [d for d in all_data if d.get("name", "").lower() == name_name.lower()]

    def read_json(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        json_path = os.path.join(base_dir, "testdata", "data.json")
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def read_json_by_name(self, name_name: str):
        all_data = self.read_json()
        return [d for d in all_data if d.get("name", "").lower() == name_name.lower()]
    def read_yaml(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        yaml_path = os.path.join(base_dir, "testdata", "data1.yaml")
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data.get("testcases",[])  # 把 testcases 列表取出来返回
    def read_yaml_by_name(self, name_name: str):
        all_data = self.read_yaml()
        return [d for d in all_data if d.get("name", "").lower() == name_name.lower()]

if __name__ == '__main__':
    rd = ReadData()
    #=================excel=======================================================================================================
    #打印全部
    # all_data = rd.read_excel()
    # print(f"📄 全部测试用例共 {len(all_data)} 条")

    # # 按模块读取示例
    # login_data = rd.read_excel_by_name("login")
    # print(f"🔍 login模块用例共 {len(login_data)} 条")
    # #register
    # login_data = rd.read_excel_by_name("register")
    # print(f"🔍register模块用例共 {len(login_data)} 条")
    # #get_user_info
    # login_data = rd.read_excel_by_name("get_user_info")
    # print(f"🔍profile模块用例共 {len(login_data)} 条")
    # #get_product
    # login_data = rd.read_excel_by_name("get_product")
    # print(f"🔍get_product模块用例共 {len(login_data)} 条")
    # #submit_order
    # login_data = rd.read_excel_by_name("submit_order")
    # print(f"🔍submit_order模块用例共 {len(login_data)} 条")
    # #get_orders
    # login_data = rd.read_excel_by_name("get_orders")
    # print(f"🔍get_orders模块用例共 {len(login_data)} 条")
    # #update_user_info
    # login_data = rd.read_excel_by_name("update_user_info")
    # print(f"🔍update_user_info模块用例共 {len(login_data)} 条")

#=========================json===================================================================================================
    # print(f"📄 全部 YAML 用例数：{len(rd.read_yaml())}")
    # print(f"🔍 登录模块 YAML 用例：{rd.read_yaml_by_name('login')}")
    #
    # print(f"📄 全部 JSON 用例数：{len(rd.read_json())}")
    # print(f"🔍 注册模块 JSON 用例：{rd.read_json_by_name('register')}")
    #
    # print(f"📄 全部 EXCEL 用例数：{len(rd.read_excel())}")
    # print(f"🔍 订单模块 EXCEL 用例：{rd.read_excel_by_name('get_orders')}")

#=====================================yaml==================================================================================
    print(f"📄 获取全部用例数：{len(rd.read_yaml())}")
    #register
    print(f"📄 获取全部用例===：{rd.read_yaml()[0]}")
    print(f"🔍 获取register模块用例：{rd.read_yaml_by_name('register')}")
    # print(f"🔍 获取login模块用例：{rd.read_yaml_by_name('login')}")
    # print(f"🔍 获取profile模块用例：{rd.read_yaml_by_name('profile')}")
    # print(f"🔍 获取get_product模块用例：{rd.read_yaml_by_name('get_product')}")
    # print(f"🔍 获取submit_order模块用例：{rd.read_yaml_by_name('submit_order')}")
    # print(f"🔍 获取get_orders模块用例：{rd.read_yaml_by_name('get_orders')}")
    # print(f"🔍 获取update_user_info模块用例：{rd.read_yaml_by_name('update_user_info')}")
