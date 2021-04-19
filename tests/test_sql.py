# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/16 11:07
@Auth ： jiejia
@File ：test_sql.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import requests
import pymysql
import pytest
from tools.conndata import Test_DButil
test_db=Test_DButil()
# def test_db_de():
#     y = test_db.test_link_mysql()
#     x = test_db.test_delete(table="manager", field="username"+"=" + "'" + '测试不停'+ "'")
    # table = 'table' in kwargs and kwargs['table'] or '*'
    #     field = 'field' in kwargs and kwargs['field'] or '*'
    #     where = 'where' in kwargs and kwargs['where']
    #     sql = 'delete from %s where %s'%(table,field)

def test_sech_createsuccess():
    test_dbtil = Test_DButil()
    # test_link=test_dbtil.test_link_mysql()
    cs = test_dbtil.test_selectsingle(field="name", table="manager", where="username"+"="+"'"+"testuser-勿删1"+"'")
    print(cs)
    # cs = cs[0]
    # print(cs)
    """删除刚刚已经创建好的用户，再进行查询，看是否删除成功"""
    test_dbtil.test_delete(table="manager", field="username"+"=" + "'" + "testuser-勿删1" + "'")
    res = test_dbtil.test_selectsingle(field="name", table="manager", where="username"+"="+"'"+"testuser-勿删1"+"'")
    assert res is None



    # 'delete from manager where username=\'\''
