# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/11 15:29
@Auth ： jiejia
@File ：test_skip.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""测试"""
"""使用pytest.skip("skip 方法名")跳过某个方法的执行"""
import pytest
from tests import test_Calculator
calcul=test_Calculator.TestCalculator()
class TestSkip():
    def sum(self,a,b):
        print(a +b )
        return a + b

    def mul(self,a,b):
        print(a - b)
        return a - b
# """使用pytest.skip("skip 方法名")"""
    def test_sum(self):
        pytest.skip("skip sum")
        print(self.sum(1,2))

    def test_mul(self):
        print(self.mul(2,1))




