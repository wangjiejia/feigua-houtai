# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/29 11:06
@Auth ： jiejia
@File ：manager_alter.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""修改用户的账户资料"""
from tools.gettoken import test_getToken
import requests
import os
import pytest
import datetime
basic_test_getToken = test_getToken()
import string,random
# url = "https://live-admin-qa1.youfenba.com/api/v1/manager/1099"
headers = {'Content-Type':'multipart/form-data'}

def test_setup_function():
    """获取上传图片的token"""
    global str
    url1 = "https://live-admin-qa1.youfenba.com/api/v1/qiniu/static_token"
    res = requests.get(url=url1,headers=headers)
    r = res.json()
    token = (r['data'])['token']
    cur = datetime.datetime.now()
    year=str(cur.year)
    mouth=str(cur.strftime('%m'))
    day=str(cur.day)
    "/douyin_livetools_admin/20210429/" + "/"
    str = []
    baseStr = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(14):
        str.append(random.choice(baseStr))
        randomStr = ''.join(str)
    key = "/douyin_livetools_admin/" +year+mouth+day +"/"+randomStr
    print(key)
    url2 = "https://upload.qbox.me/"
    dict = {
        "token":token,
        "key":key,
        "file":('账户资料上传的文件.jpg',open(r'C:/Users/1/PycharmProjects/feigua-houtai/file/账户资料上传的文件.jpg','rb'),'image/png')
    }
    res = requests.post(url=url2,data=dict,headers={'Content-Type':'multipart/form-data;boundary=<calculated when request is sent>'})
    r=res.json()
    print(r)

# def test_manager_alter():
#     dict={
#         "company":"test_company",
#         "company_short":"test公司简称",
#         "logo":logo_url,
#         "password":"admin",
#         "remark":"test备注",
#         "username":"18230526256"
#     }
#     res = requests.put(url=url,data=dict,headers=headers)
#     r = res.json()
#     print(r)
