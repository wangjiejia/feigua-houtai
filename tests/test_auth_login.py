# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/6 11:28
@Auth ： jiejia
@File ：test_auth_login.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""运营后台直登前台账户"""
"""测试测试"""
from tools.gettoken import test_headers
import requests
import pytest
from tools.test_user import test_createsuccess
headers=test_headers()
"""获取直登用户的token"""
def test_auth_login():
    ID = str(test_createsuccess())
    url1 = "https://live-admin-qa1.youfenba.com/api/v1/auth_login/"
    url = url1 + ID
    # print(url)
    res = requests.get(url=url,headers=headers)
    r=((res.json())['data'])['token']
    # print(r)
    """能获取到抖音号列表，即表示直登成功"""
    auth_headers = {'user-agent': 'Mozilla/5.0', 'Authorization': 'Bearer {0}'.format(r)}
    login_url="https://live-tools-qa1.youfenba.com/api/v1/douyin?limit=10&page=1"
    res1 = requests.get(url=login_url,headers=auth_headers)
    r1=res1.json()
    assert r1['code'] == 200


if __name__=='__main__':
    pytest.main(['test_auth_login.py'])







