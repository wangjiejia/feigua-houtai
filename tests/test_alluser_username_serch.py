# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/9 15:34
@Auth ： jiejia
@File ：zengyi.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from tests.Test_get_yml_data import Test_get_yml_data
import sys
x = Test_get_yml_data()
def test_username_serch():
    name = sys._getframe().f_code.co_name
    # y = x.test_alluser_serch(sys._getframe().f_code.co_name)
    r1=x.test_get_yml(name=name)
    assert r1['code'] == 200
    assert (((r1['data'])['list'])[0])['username'] == "17706531630"











