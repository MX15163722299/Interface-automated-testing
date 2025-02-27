import os,json

# json_path = os.path.dirname(os.path.dirname(__file__)) + "/testData/data.json"

# json_path = os.path.dirname(os.path.dirname(__file__))
# print(json_path)

json_path = os.path.dirname(os.path.dirname(__file__)) + "/testData/data.json"
 #1.2 打开json文件
with open(json_path,'r') as f:
    #1.3 将json 转化为字典并且存到变量里面
    data = json.load(f)
    print(data.values())
    #1.4 读取字典内所有的value 转化为列表
    testdata1 = list(data.values())
    # print(testdata1)