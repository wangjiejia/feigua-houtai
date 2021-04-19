# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/29 10:00
@Auth ： jiejia
@File ：conftest.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""先进行登录，获取登录成功后的token"""
import requests
import pytest


"""'Authorization':'Bearer {0}'.format(getToken()),"""
"""@pytest.ficture()标记，该函数可作为一个参数进行传递"""


def test_getToken():
    dict1 = {'username': 'admin', 'password': '123123'}
    r = requests.post(
        url='https://live-admin-qa1.youfenba.com/api/v1/login',
        json=dict1,
        headers={'user-agent': 'Mozilla/5.0'}
    )
    headers=((r.json())['data'])['token']
    print(headers)
    return headers
def test_headers():
    token = test_getToken()
    headers = {'user-agent': 'Mozilla/5.0','Authorization': 'Bearer {0}'.format(token)}
    return headers

    # print( {'user-agent': 'Mozilla/5.0', 'Authorization': 'Bearer {0}'.format(test_getToken())})
#
# @pytest.fixture()
# def headers():
#     return  {'user-agent': 'Mozilla/5.0', 'Authorization': 'Bearer {0}'.format(test_getToken())}
if __name__=='__main__':
    pytest.main(['gettoken.py'])