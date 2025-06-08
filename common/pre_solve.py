import json
import re
from jsonpath import jsonpath
from common.config_http import ConfigHttp

# 模拟响应结构统一封装（兼容 header 和 json）
class DummyResponse:
    def __init__(self, json_data, headers=None):
        self._json = json_data
        self.headers = headers or {}

    def json(self):
        return self._json


class PreSolve:
    def __init__(self, all_test_data):
        self.all_data = all_test_data  # 所有测试用例
        self.res_dict = {}             # 缓存所有已执行过的前置响应

    def preSolve(self, dic):
        # 1. 获取所有 ${id:field} 格式的占位符
        pattern = re.compile(r"\${(\d+):(.+?)}")
        all_placeholders = pattern.findall(json.dumps(dic))

        # 2. 去重并遍历依赖ID，执行依赖接口
        for dep_id, _ in set(all_placeholders):
            self.execute_dependency(dep_id)

        # 3. 替换当前接口的 value 和 header
        header, value = self.process_row(dic, self.res_dict)

        # 4. 替换结果写回原字典（注意类型转换）
        dic["header"] = json.dumps(header, ensure_ascii=False) if isinstance(header, dict) else header
        dic["value"] = json.dumps(value, ensure_ascii=False) if isinstance(value, dict) else value

        return header, value

    def execute_dependency(self, dep_id):
        if dep_id in self.res_dict:
            return  # 已执行，跳过

        dep_case = next(
            (case for case in self.all_data
             if str(int(float(case.get("id", -1)))) == dep_id),
            None
        )

        if not dep_case:
            print(f"❌ 未找到依赖的用例 ID={dep_id}")
            return

        print(f"🚀 执行依赖用例 ID={dep_id}，接口：{dep_case.get('name')}")
        ch = ConfigHttp(dep_case)
        response = ch.run()

        try:
            res_json = response.json()
        except:
            res_json = {}

        self.res_dict[dep_id] = DummyResponse(res_json, response.headers)

    @classmethod
    def recursive_replace(cls, data, res_dict):
        pattern = re.compile(r"\${(\d+):(.+?)}")

        if isinstance(data, str):
            matches = pattern.findall(data)
            for case_id, field in matches:
                response = res_dict.get(case_id)
                if not response:
                    continue

                if field.lower() == "set-cookie":
                    raw_cookie = response.headers.get("Set-Cookie", "")
                    val = raw_cookie.split(";")[0]  # ⚠️ 仅取 uid=u001
                else:
                    val = jsonpath(response.json(), f"$..{field}")
                    val = val[0] if val else ""

                data = data.replace(f"${{{case_id}:{field}}}", str(val))
            return data

        elif isinstance(data, dict):
            return {k: cls.recursive_replace(v, res_dict) for k, v in data.items()}

        elif isinstance(data, list):
            return [cls.recursive_replace(i, res_dict) for i in data]

        return data

    @classmethod
    def process_row(cls, row_dict, res_dict):
        try:
            raw_value = row_dict.get("value", "{}") or "{}"
            raw_header = row_dict.get("header", "{}") or "{}"

            try:
                value = json.loads(raw_value)
            except Exception:
                value = raw_value

            try:
                header = json.loads(raw_header)
            except Exception:
                header = raw_header

            replaced_value = cls.recursive_replace(value, res_dict)
            replaced_header = cls.recursive_replace(header, res_dict)

            print(f"✅ 替换后 header: {replaced_header}")
            print(f"✅ 替换后 value: {replaced_value}")

            return replaced_header, replaced_value

        except Exception as e:
            print(f"❌ 用例处理失败：{e}")
            return {}, {}

if __name__ == '__main__':
    from common.readData import ReadData
    rd = ReadData()
    data = rd.read_excel()

    ps = PreSolve(data)
    row_data = data[6]  # 用例行数据
    value, header = ps.preSolve(row_data)

    from common.config_http import ConfigHttp
    ch = ConfigHttp(row_data)
    response = ch.run()
    print(f"✅ 响应: {response.text}")
    print(row_data)
