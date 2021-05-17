# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/17 15:37
@Auth ： jiejia
@File ：test_moudle.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""pytest.freeze_includes打印出所有模块名称"""
import pytest
import sys

def test_freeze():
    print(pytest.freeze_includes())