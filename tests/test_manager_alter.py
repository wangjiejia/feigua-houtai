# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/29 11:06
@Auth ： jiejia
@File ：manager_alter.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""修改用户的账户资料"""
from tools.gettoken import test_headers
import requests
import os
import pytest
headers = test_headers()
url = "https://live-admin-qa1.youfenba.com/api/v1/manager/1099"

def setup_function():
    url1 = "https://live-admin-qa1.youfenba.com/api/v1/qiniu/static_token"
    res = requests.get(url=url)
    print(res)
    url2 = "https://upload.qbox.me/"
    dict = {
        "token":"",
        "key":"",
        "file":"(binary)"
    }
    res = requests.post(url=url,)

def test_manager_alter():
    dict={
        "company":"test_company",
        "company_short":"test公司简称",
        "logo":"/douyin_livetools_admin/20210429/RFSQ-NChBaWC7G-RJT-SrCSEhcnSN7-n",
        "password":"admin",
        "remark":"test备注",
        "username":"18230526256"
    }
    res = requests.put(url=url,data=dict,headers=headers)
    r = res.json()
    print(r)
