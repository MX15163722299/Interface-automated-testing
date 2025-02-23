import random

import pytest
# def test_case001():
#     print("\n执行测试用例 1")
#     assert 1 == 2,"两个数不相等"


class TestCase:
    def test_case001(self):
        print("执行测试用例 1")
        assert random.choice(['Ture','False'])

    def test_case002(self):
        print("这是测试用例 2")
        assert 2 == 2,"两个数相等"
if __name__ == '__main__':
    # pytest.main(['-v','test_case.py::TestCase::test_case002','-n=2'])
    pytest.main(['-v','-reruns=2'])