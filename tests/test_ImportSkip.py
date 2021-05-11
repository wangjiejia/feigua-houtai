# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/11 15:52
@Auth ： jiejia
@File ：test_ImportSkip.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import pytest
import selenium
from tests.test_Calculator import TestCalculator
calcul=TestCalculator()
class Test_ImportSkip():
    def sum(self,a):
        return a+1

    """pytes.importorskip("模块名")校验，如果没有导入模块selenium的话，不会执行该用例，如果导入了selenium的话，就执行接下来的步骤"""
    def test_ImportSkip(self):
        sele=pytest.importorskip("selenium")
        print(sele)
        print("skip this sum",self.sum(5))



