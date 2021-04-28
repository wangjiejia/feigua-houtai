# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/20 9:39
@Auth ： jiejia
@File ：test_create_user.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""运营后台创建用户"""
import requests
import pytest
from tools.gettoken import test_headers
from tools.conndata import Test_DButil
headers = test_headers()
url = "https://live-admin-qa1.youfenba.com/api/v1/manager"
def test_createsuccess():
    dict1 = {
        "company": "company-勿删",
        "company_short": "testcompany-勿删",
        "logo": "1",
        "password": "123123",
        "username": "testuser-勿删1"}
    r = requests.post(url=url, json=dict1, headers=headers)
    succ_username=((r.json())['data'])['username']
    test_dbtil = Test_DButil()
    test_link=test_dbtil.test_link_mysql()
    return succ_username,id