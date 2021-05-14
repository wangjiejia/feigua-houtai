# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/14 15:40
@Auth ： jiejia
@File ：test_exit.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""pytest.exit("测试结束")，结束该条用例"""
import pytest
import requests


def sum(a):
    sum = a + 1
    print(sum)

def test_sum1():
    print(sum(3))


def test_sum2():
    print(sum(4))
    pytest.exit("结束结束")

def test_sum3():
      print(sum(5))

