# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/10 17:13
@Auth ： jiejia
@File ：wjj_test.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""参数化测试用例"""
from tools.gettoken import test_headers
import requests
import pytest
from tests.test_Calculator import TestCalculator
headers=test_headers()
calcul=TestCalculator()

def test_function():
    pass
def test_add(a,b):
    res = a + b
    return res
@pytest.fixture(scope="class")
def test_print_log():
    print("计算开始")
    yield
    print("计算结束")

class TestCalc():
    def setup_class(self):
        print("计算开始")
        self.calc= TestCalculator()

    def teardown(self):
        print("计算完毕")


        # def setup_class(self):
        #     print("计算开始")
        #     # 实例化计算器类
        #     self.calc = Calculator()
        #
        # def teardown_class(self):
        #     print("计算完毕")


            @pytest.mark.parametrize(
                "a, b, expect",
                [
                    (1, 1, 2),
                    (0.1, 0.1, 0.2),
                    (-1, -1, -2)
                ], ids=['int', 'float', 'negative']
            )
            def test_add(self, get_calc, a, b, expect):
                result = get_calc.add(a, b)
                # 得到相加结果之后，写断言
                assert result == expect

            @pytest.mark.usefixtures('print_log')
            def test_add1(self, get_calc):
                result = get_calc.add(0.1, 0.1)
                # 得到相加结果之后，写断言
                assert result == 0.2

            def test_add2(self, get_calc):
                # 实例化计算器类
                # calc = Calculator()
                result = get_calc.add(-1, -1)
                # 得到相加结果之后，写断言
                assert result == -22


