# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/11 16:25
@Auth ： jiejia
@File ：test_fail.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""pytest.xfail(标识失败）标记这个用例已经失败，不用再执行"""
import pytest
import requests
class TestFail():
    def sum(self,a):
        return a + 2

    def test_fail(self):
        pytest.xfail("标识失败")
        print(sum(3))