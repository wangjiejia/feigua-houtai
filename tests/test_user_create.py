# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/30 15:35
@Auth ： jiejia
@File ：user_create.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import requests
import pytest
from tools.gettoken import test_headers
from tools.conndata import Test_DButil
url = "https://live-admin-qa1.youfenba.com/api/v1/manager"

headers=test_headers()
def test_userisnull():
    dict1 = {
     "company":"company",
    "company_short":"testcompany",
    "logo":"1",
    "password":"123123",
    "username":""}
    r=requests.post(url=url,json=dict1,headers=headers)
    res=r.json()
    print(res)
    assert res['message'] == "账户名必填"

def test_passisnull():
    dict1 = {
     "company":"company",
    "company_short":"testcompany",
    "logo":"1",
    "password":"",
    "username":"admin"}
    r=requests.post(url=url,json=dict1,headers=headers)
    res=r.json()
    print(res)
    assert res['message'] == "密码必填"

def test_companyshortisnull():
    dict1 = {
     "company":"company",
    "company_short":"",
    "logo":"1",
    "password":"123123",
    "username":"admin"}
    r=requests.post(url=url,json=dict1,headers=headers)
    res=r.json()
    print(res)
    assert res['message'] == "公司简称必填"

def test_companyisnull():
    dict1 = {
     "company":"",
    "company_short":"testcompany",
    "logo":"1",
    "password":"123123",
    "username":"admin"}
    r=requests.post(url=url,json=dict1,headers=headers)
    res=r.json()
    print(res)
    assert res['message'] == "公司名称必填"
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
    cs = test_dbtil.test_selectsingle(field="id", table="manager", where="username"+"="+"'"+succ_username+"'"+"and" +" "+"deleted_at" + " "+ "is" +" "+ "null")
    # cs = cs[0]
    print(cs)
    cs = str(cs)
    test_dbtil.test_delete(table="manager", field="username" + "=" + "'" + succ_username + "'")
    return succ_username
def test_sech_createsuccess():
    usern=test_createsuccess()
    print(usern)
    test_dbtil = Test_DButil()
    # test_link=test_dbtil.test_link_mysql()
    cs = test_dbtil.test_selectsingle(field="name", table="manager", where="username"+"="+"'"+usern+"'")
    print(cs)
    test_dbtil.test_delete(table="manager", field="username"+"=" + "'" + usern + "'")
    res = test_dbtil.test_selectsingle(field="name", table="manager", where="username"+"="+"'"+usern+"'")
    assert res is None


    # test_dbtil.test_delete(table="manager",field="username",where="'" + cs + "'")

    # sql = 'delete from %s where %s = %s' % (table, field, where)
    # table = 'table' in kwargs and kwargs['table'] or '*'
    # field = 'field' in kwargs and kwargs['field'] or '*'
    # where = 'where' in kwargs and kwargs['where'] or '*'


def test_userisexit():
    dict1 = {
        "company": "company-勿删",
        "company_short": "testcompany-勿删",
        "logo": "1",
        "password": "123123",
        "username": "testuser-勿删1"}
    r = requests.post(url=url, json=dict1, headers=headers)
    res = r.json()
    print(res)
    assert res['message'] == "该账户名已存在"






