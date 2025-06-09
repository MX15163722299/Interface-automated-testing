"""
定义一一个类
1.定义初始化方法：
    1.1获取预期结果
    1.2获取返回的实际结果
    1.3先断言接口的状态码
2.定义一个对外的断言方法
    1.1 断言状态码是否正确
    1.2 循环断言字典里面的键值对
"""
from jsonpath import jsonpath

class PublicAssert:
# 1.定义初始化方法：
    def __init__(self,dic,res,db = None):
        if "expect" in dic:  # 是完整 test_data dict
            dic = dic["expect"]

        if isinstance(dic, str):
            try:
                dic = eval(dic)  # 👈 如果是字符串，转成 dict
            except Exception as e:
                raise ValueError(f"❌ 断言数据解析失败，请检查 expect 格式是否正确：{e}")

        self.interface_expect = dic.get("interface_assert", {})
        self.db_expect = dic.get("db_assert", {})
        self.res = res.json()
        self.status = res.status_code
        self.db = db


        # print(f"预期结果{self.dic}")
        # print(f"实际结果{self.res}")
        # print(f"状态码{self.status}")
        # print(f"db{self.db}")


# 2.定义一个对外的断言方法
    def public_assert(self):
        assert self.status in [200, 304, 201], f"❌ 接口请求失败，状态码：{self.status}"
        msg = ""

        for k, v in self.interface_expect.items():
            real = jsonpath(self.res, f"$..{k}")
            if not real:
                msg += f"\n❌ 接口返回中未找到字段：{k}"
            elif str(v) != str(real[0]):
                msg += f"\n❌ 字段【{k}】断言失败：预期 {v}，实际 {real[0]}"

        if self.db_expect and self.db:
            sql = self.db_expect.get("sql")
            expected = str(self.db_expect.get("expect"))
            result = self.db.query(sql)
            if not result:
                msg += f"\n❌ 数据库查询无返回，SQL：{sql}"
            else:
                actual = str(result[0][0])
                if actual != expected:
                    msg += f"\n❌ 数据库断言失败：期望 {expected}，实际 {actual}"
        elif self.db_expect and not self.db:
            msg += "\n⚠️ 用例包含数据库断言，但未传入 db 连接"

        # assert msg == "",msg
        # ...之前的断言累加逻辑...

        if msg:
            print("❌ 断言失败，详情如下：")
            print(msg)
            raise AssertionError(msg)  # ✅ 保证 main.py 调用时也能中断


if __name__ == '__main__':
    from common.read_data import ReadData
    from common.mysql_client import MySQLClient
    from common.conf_test import db
    rd = ReadData()
    testdata = rd.read_excel()
    print(f"测试数据{testdata[1]}")
    print(f"预期结果{testdata[1]['expect']}")
    # print({testdata[6]["expect"])
    from common.config_http import ConfigHttp
    chttp = ConfigHttp(testdata[1])
    res = chttp.run()
    print(f"实际结果{res.json()}")
    # mysql = MySQLClient()

    # print(f"数据库结果{db}")
    p = PublicAssert(testdata[1]['expect'],res,db)
    p.public_assert()




