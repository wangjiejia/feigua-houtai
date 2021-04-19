# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/3 15:06
@Auth ： jiejia
@File ：delete_user.py
@IDE ：PyCharm
"""
import requests
import pytest
import pymysql
"""通过 user_create创建成功的用户，再通过这个类进行删除"""
from tools.gettoken import test_headers
headers=test_headers()
from tests.test_user_create import test_createsuccess
ID = str(test_createsuccess())
url1 = "https://live-admin-qa1.youfenba.com/api/v1/manager/"
url = url1 +ID
print(url)
def test_delete():
    print(url)
    res=requests.delete(headers=headers,url=url)
    r= res.json()
    print(r)
    assert r['code'] == 200


