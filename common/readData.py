import xlrd
import os

from pipenv.patched.safety.formatters import json
from pipenv.vendor.ruamel import yaml

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
        self.path_name = os.path.dirname(os.path.dirname(__file__)) + "/testData/data.xls"
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
            rew_value = self.sheet.cell_value(i,0)
            #组装成为一个字典
            dict1 = dict(zip(self.first_row,rew_value))
            #组装好的字典放到列表里面
            self.res_list.append(dict1)
        #将结果返回
        return self.res_list

    def read_json(self):
        #1.1 获取文件路径
        json_path = os.path.dirname(os.path.dirname(__file__)) + "/testData/data.json"
        #1.2 打开json文件
        with open(json_path,'r') as f:
            #1.3 将json 转化为字典并且存到变量里面
            testdata = json.load(f)
            #1.4 读取字典内所有的value 转化为列表
            testdata1 = list(testdata.values())
        return testdata1

    def read_yaml(self):
        yaml_path = os.path.dirname(os.path.dirname(__file__)) + "/testData/data.yaml"
        with open(yaml_path,'r') as f:
            testdata = yaml.load(f)
            testdata2 = list(testdata.values())
        return testdata2


'''
2.定义一个组装数据的对外方法：read_json
    2.1 获取文件路径
    2.2 打开json文件
    2.3 将json转化为字典，并纯在变量里面
    2.4 关闭json文件
    2.5 读取字典内所有的value 转化为列表
    2.6 返回组装好的列表
'''


'''

class ReadData:
    def __init__(self):
        #获取文件路径
        self.path_name = os.path.dirname(os.path.dirname(__file__)) + "/testData/data.xls"
        print(self.path_name)
        #打开并读取 excel

        self.read_book = xlrd.open_workbook(self.path_name)

        #读取指定的 sheet页

        self.sheet = self.read_book.sheet_by_index(0)

        #读取最大行和最大列

        self.max_row = self.sheet.nrows
        self.max_col = self.sheet.ncols

        #预设一个返回列表。默认为空

        self.res_list = []

        #获取第一行作为列表的 key

        self.first_row = self.sheet.row_values(0)

    def read_excel(self):
        #循环读取每一行作为一条测试用例
        for i in range(1,self.max_row):
            row_value = self.sheet.row_values(i)
            dict1 = dict(zip(self.first_row,row_value))
            self.res_list.append(dict1)
            return self.res_list
        

def read_json       
        
        
if __name__ == '__main__':
    R = ReadData()
    print(R.read_excel())



# script_dir = os.path.dirname(os.path.abspath(__file__))
# script_dir = os.path.dirname(script_dir)
# # print(script_dir)
# script_dir = script_dir + "/testData/data.xls"
# print(script_dir)
# #打开 excel文件
# readbook = xlrd.open_workbook(script_dir)
# #获取所有sheet页的名字
# sheet = readbook.sheet_by_index(0)
# print(sheet)
# #获取 sheet页的最大行/列
# max_row = sheet.nrows
# max_col = sheet.ncols
# print(f"最大行数是：{max_row}\n最大列数是：{max_col}")
# #获取某个单元格的值
# print(sheet.cell_value(0,0))
# #获取某行某列的值
# print(sheet.row_values(0))
# print(sheet.col_values(1))


'''