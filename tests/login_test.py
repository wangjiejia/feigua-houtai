# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/18 13:43
@Auth ： jiejia
@File ：login1_test.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import pytest
import requests

headers = {'user-agent': 'Mozilla/5.0'}
url = "https://live-admin-qa1.youfenba.com/api/v1/login"
class Test_login():
    def test_login_success(self):
        name = sys._getframe().f_code.co_name
        # y = x.test_alluser_serch(sys._getframe().f_code.co_name)
        r1 = x.test_get_yml(name=name)
        assert r1['code'] == 200
        assert (((r1['data'])['list'])[0])['username'] == "17706531630"
        # data = (('username', 'admin'), ('password', '123123'))
        # r = requests.post(url=url, headers=headers, data=data)
        # res = r.json()
        # print(res['code'])
        # assert res['code'] == 200
    def test_login_nousername(self):
        data = (('username', '  '), ('password', '123123'))
        r = requests.post(url=url, headers=headers, data=data)
        res = r.json()
        # print(res['message'])
        assert res['message'] == "账户名必填"

    def test_login_no_passwd(self):
        data = (('username', 'admin'), ('password', '   '))
        r = requests.post(url=url, headers=headers, data=data)
        res = r.json()
        # print(res['message'])
        assert res['message'] == "密码必填"

    def test_login_username_error(self):
        data = (('username', 'admin1'), ('password', '123123'))
        r = requests.post(url=url, headers=headers, data=data)
        res = r.json()
        # print(res['message'])
        assert res['message'] == "用户名不存在"

    def test_login_passwd_error(self):
        data = (('username', 'admin'), ('password', '123456'))
        r = requests.post(url=url, headers=headers, data=data)
        res = r.json()
        # print(res['message'])
        assert res['message'] == "密码不正确"
    #
    # def test_getToken(self):
    #     dict1 = {'username': 'admin', 'password': '123123'}
    #     r = requests.post(
    #         url='https://live-admin-qa1.youfenba.com/api/v1/login',
    #         json=dict1
    #     )
    #     print(r.json())
    #     return (r.json()['data'])['token']

if __name__ == '__main__':
    pytest.main(['login1_test.py'])












