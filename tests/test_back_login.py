# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/6 11:41
@Auth ： jiejia
@File ：test_login.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""后台登录测试"""
import requests
import pytest
url = "https://live-admin-qa1.youfenba.com/api/v1/login"
headers = {'user-agent': 'Mozilla/5.0'}
def test_useriserror():
    dict1={"username": "admin1","password": "123123"}
    res=requests.post(url=url,data=dict1)
    r=res.json()
    assert r['message'] == "用户名不存在"

def test_passiserror():
    dict1 = {"username": "admin", "password": "123111"}
    res = requests.post(url=url, data=dict1)
    r = res.json()
    assert r['message'] == "密码不正确"
    print(r)

def test_userisnull():
    dict1 = {"username": "", "password": "123111"}
    res = requests.post(url=url, data=dict1)
    r = res.json()
    assert r['message'] == "账户名必填"
    print(r)

def test_passisnull():
    dict1 = {"username": "admin", "password": ""}
    res = requests.post(url=url, data=dict1)
    r = res.json()
    assert r['message'] == "密码必填"
    print(r)

def test_back_login():
    dict1 = {"username": "admin", "password": "123123"}
    res = requests.post(url=url, data=dict1)
    r = res.json()
    assert r['code'] == 200
    print(r)

if __name__=='__main__':
    pytest.main(['test_back_login.py'])
