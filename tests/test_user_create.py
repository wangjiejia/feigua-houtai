# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/30 15:35
@Auth ： jiejia
@File ：user_create.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""运营后台创建用户"""
import requests
import pytest
from tools.gettoken import test_headers
from tools.conndata import Test_DButil
from tools.test_user import test_createsuccess
url = "https://live-admin-qa1.youfenba.com/api/v1/manager"
headers=test_headers()
test_dbtil = Test_DButil()
"""账户名为空"""
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
"""密码为空"""
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
""" 公司简称为空"""
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
"""公司名称为空 """
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

""" 用户创建成功 """
def test_sech_createsuccess():
    username = test_createsuccess()
    usern= test_dbtil.test_selectsingle(field="name", table="manager", where="username"+"="+"'"+ username + "'")
    print(usern)
    assert usern[0] == "管理员"
    test_link=test_dbtil.test_link_mysql()
    test_dbtil.test_delete(table="manager", field="username"+"=" + "'" + usern + "'")
    res = test_dbtil.test_selectsingle(field="name", table="manager", where="username"+"="+"'"+usern+"'")
    assert res is None
"""用户已存在 """

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
    pytest.xfail("该账户名已存在，所以不需要执行")
    assert res['message'] == "该账户名已存在11111"
#
"""删除用户的接口"""
def test_delete():
    id = test_dbtil.test_selectsingle(field="id", table="manager",where="username" + "=" + "'" + "testuser-勿删1" + "'" + "and deleted_at is null ")
    id = id[0]
    id = str(id)
    url = "https://live-admin-qa1.youfenba.com/api/v1/manager/" + id
    print(url)
    r = requests.delete(url=url,headers=headers)
    res = r.json()
    print(res)
    assert res['code'] == 200

"""删除该用户后，在列表中查询不存在"""
def test_deleted_sech():
    id = test_dbtil.test_selectsingle(field="id", table="manager",  where="username" + "=" + "'" + "testuser-勿删1" + "'"+ "and deleted_at is null ")
    assert id is None
    """删除用户后，在数据库中清除创建的数据"""
    test_dbtil.test_delete(table="manager",field="username"  + "=" + "'" + "testuser-勿删1" + "'")








    # test_dbtil.test_delete(table="manager",field="username",where="'" + cs + "'")

    # sql = 'delete from %s where %s = %s' % (table, field, where)
    # table = 'table' in kwargs and kwargs['table'] or '*'
    # field = 'field' in kwargs and kwargs['field'] or '*'
    # where = 'where' in kwargs and kwargs['where'] or '*'








