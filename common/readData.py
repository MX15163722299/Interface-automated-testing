import xlrd
import os
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