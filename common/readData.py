import xlrd
import os
import json
import yaml
'''
定义一个类
1 定义初始化方法

2.定义一个组装数据的对外方法：read_excel
    循环读取每一行作为一条测试数据（第一行除外）
    2.1 获取每一行的数据
    2.2 组装成一个字典
    2.3 将组装好的字典翻到结果列表
    2.4 将组装好的结果列表返回给调用使用    
'''
class ReadData():
    def __init__(self):
        # 1.1
        # 获取文件路径
        # self.path_name = os.path.dirname(os.path.dirname(__file__)) + "/testData/data.xls"
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.path_name = os.path.join(base_dir, "testData", "data.xls")
        print(self.path_name)
        # 1.2
        # 打开并且读取excel
        self.read_book = xlrd.open_workbook(self.path_name)

        # 1.3
        # 获取置顶的sheet页面
        self.sheet = self.read_book.sheet_by_index(0)

        # 1.4
        # 获取最大行最大列
        self.max_row = self.sheet.nrows

        self.max_col = self.sheet.ncols

        # 1.5
        # 预设一个返回列表，默认为空列表
        self.res_list = []

        #1.6 获取第一行作为列表的 key

        self.first_row = self.sheet.row_values(0)


    def read_excel(self):
        for i in range(1,self.max_row):
            # 获取每一行的数据
            rew_value = self.sheet.row_values(i,0)
            #组装成为一个字典
            dict1 = dict(zip(self.first_row,rew_value))
            #组装好的字典放到列表里面
            self.res_list.append(dict1)
        #将结果返回
        return self.res_list

    def read_json(self):
        #1.1 获取文件路径
        # json_path = os.path.dirname(os.path.dirname(__file__)) + "/testData/data.json"
        base_dir = os.path.dirname(os.path.dirname(__file__))
        json_path = os.path.join(base_dir, "testData", "data.json")
        #1.2 打开json文件
        with open(json_path,'r',encoding='utf-8') as f:
            #1.3 将json 转化为字典并且存到变量里面
            testdata = json.load(f)
            #1.4 读取字典内所有的value 转化为列表
            # testdata1 = list(testdata.values())
        return testdata

    def read_yaml(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        yaml_path = os.path.join(base_dir, "testData", "data.yaml")

        with open(yaml_path,'r',encoding='utf-8') as f:
            testdata = yaml.safe_load(f)
        return testdata

if __name__ == '__main__':
    re = ReadData()
    rep = re.read_excel()
    print(rep[6])

    res = re.read_json()
    print(res[6])

    res = re.read_yaml()
    print(res[6])



