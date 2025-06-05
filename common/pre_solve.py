#定义一个类
import re
from common.config_http import ConfigHttp
from jsonpath import jsonpath
class PreSolve:
    #定义初始化方法
    def __init__(self,testdata):
        # 获取所有测试用例并且绑定自身属性
        self.testdata = testdata
    #定义一个方法：根据当前的用例执行依赖前置并且替换依赖字段
    def preSolve(self,dic):
        rely = dic["rely"]
        caseId = dic["caseid"]
        header = dic["header"]
        value = dic["value"]
        print(f"关键字段{rely}\n{caseId}\n{header}\n{value}")
        #判断是否有依赖rely 是否为 Y,
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
        else:
            return header,value
    def get_Predata(self,data):
        # 根据正则找依赖字段
        res = re.findall(r"\${(.*?)}", data)
        if len(res) != 0:
            return res[0]
        else:
            return None
    def run_Pre(self,caseid,goal_header = None,goal_body = None):

        data = self.testdata[int(caseid)-1]
        ch = ConfigHttp(data)
        res= ch.run()
        print(res.headers)
        print(res.json())
        print(f"这是{res.headers}")
        set_cookie = res.headers.get("Set-Cookie")
        print("🍪 Set-Cookie:", set_cookie)
        if goal_header != None:
            goal_header = res.headers[goal_header]
        if goal_body != None:
            goal_body = jsonpath(res.json(),"$.."+goal_body)[0]
        return goal_header,goal_body
if __name__ == '__main__':
    from common.readData import ReadData
    rd = ReadData()
    data = rd.read_excel()
    # print(data[3])
    ps = PreSolve(data)
    print(ps.preSolve(data[4]))
    # 替换依赖值header,value
    data[4]["header"], data[4]["value"] = ps.preSolve(data[4])
    from common.config_http import Config_http
    run = Config_http.run(data[4])
    print(run.text)

    print(data[4])

