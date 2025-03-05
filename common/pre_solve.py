#定义一个类
import re
from common.configHttp import ConfigHttp
from jsonpath import jsonpath
class PreSolve:
    #定义初始化方法
    def __init__(self,testdata):
        self.testdata = testdata


    #获取所有测试用例并且绑定自身属性


    #定义一个方法：根据当前的用例执行依赖前置并且替换依赖字段
    def preSolve(self,dic):
        rely = dic["rely"]
        caseId = dic["caseid"]
        header = dic["header"]
        value = dic["value"]
        print(f"关键字段{rely}\n{caseId}\n{header}\n{value}")
        if rely.lower() == "y" and caseId != "":
            goal_header = self.get_Predata(header)
            goal_body = self.get_Predata(value)
            print(f"请求头依赖：{goal_header}\n请求体依赖：{goal_body}")
            h,b = self.run_Pre(caseId,goal_header,goal_body)
            print(f"请求头：{h}\n请求体{b}")
            if h != None:
                header = header.replace("${"+goal_header+"}",h)
            if b != None:
                value = value.replace("${"+goal_body+"}",b)
            return header,value

            #根据正则找依赖字段

        else:
            return header,value
    def get_Predata(self,data):
        res = re.findall(r"\${(.*?)}", data)

        if len(res) != 0:
            return res[0]
        else:
            return None
    def run_Pre(self,caseid,goal_header = None,goal_body = None):

    #判断是否有依赖rely 是否为 Y,
        data = self.testdata[int(caseid)-1]
        ch = ConfigHttp(data)
        res = ch.run()
        print(res.headers)
        print(res.json())

        if goal_header != None:
            goal_header = res.headers[goal_header]
        if goal_body != None:
            goal_body = jsonpath(res.json(),"$.."+goal_body)[0]
        return goal_header,goal_body



    #没有依赖直接获取入参值value

if __name__ == '__main__':
    from common.readData import ReadData
    rd = ReadData()
    data = rd.read_excel()
    # print(data[3])
    ps = PreSolve(data)
    print(ps.preSolve(data[3]))
    #
    # str1 = "{'name':'${username}','link':'www.baidu.com'}"
    # str2 = '{"cookie":"${Set-Cookie}"}'
    # str3 = "123"
    # print(ps.get_Predata(str1))
    # print(ps.get_Predata(str2))
    # print(ps.get_Predata(str3))

    # print(ps.run_Pre("1", goal_header="Set-Cookie",goal_body="username"))
