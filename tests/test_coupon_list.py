# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/6 11:35
@Auth ： jiejia
@File ：test_coupon_list.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from tools.gettoken import test_headers
import requests
ids=[]
headers=test_headers()
basic_url = "https://live-admin-qa1.youfenba.com/api/v1/coupon?limit=50&page=1&name=%E2%80%9C%E6%8E%A5%E5%8F%A3%E6%B5%8B%E8%AF%95%E2%80%9D"
"""状态为未使用的F码"""
def test_sech1():
    url = basic_url + "&" +"status" +"=" +"0"
    print(url)
    res = requests.get(url=url,headers=headers)
    r=res.json()
    x = len((r['data'])['list'])
    print(x)
    ids = []
    for i in range (0,x):
        ids1 = (((r['data'])['list'])[i])['id']
        ids.append(ids1)
    print(str(ids))
    b = [str(j) for j in ids]
    # str2 = ''.join(b)
    c = (',').join(str(x) for x in b)
    d = '"'+c+'"'
    print(d)
    assert (((r['data'])['list'])[0])['id'] is not None
    return d



"""筛选状态为已核销的F码"""
def test_sech2():
    url = basic_url + "&" +"status" +"="+"1"
    print(url)
    res = requests.get(url=url,headers=headers)
    r=res.json()
    print(r)
    assert len((r['data'])['list'])  == 0

"""筛选状态为已锁定的F码"""
def test_sech3():
    url = basic_url + "&" +"status" +"="+"2"
    print(url)
    res = requests.get(url=url,headers=headers)
    r=res.json()
    print(r)
    assert len((r['data'])['list'])  == 0





