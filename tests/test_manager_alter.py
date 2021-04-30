# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/29 11:06
@Auth ： jiejia
@File ：manager_alter.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""修改用户的账户资料"""
from tools.gettoken import test_getToken,test_headers
import requests
import os
import pytest
import datetime
basic_test_getToken = test_getToken()
import string,random

headers=test_headers()


def test_setup_function():
    basic_headers = {'Content-Type': 'multipart/form-data'}
    """获取上传图片的token"""
    global str
    url1 = "https://live-admin-qa1.youfenba.com/api/v1/qiniu/static_token"
    res = requests.get(url=url1,headers=basic_headers)
    r = res.json()
    token = (r['data'])['token']
    cur = datetime.datetime.now()
    year=str(cur.year)
    mouth=str(cur.strftime('%m'))
    day=str(cur.day)
    "/douyin_livetools_admin/20210429/" + "/"
    str = []
    baseStr = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(32):
        str.append(random.choice(baseStr))
        randomStr = ''.join(str)
    key = "/douyin_livetools_admin/" +year+mouth+day +"/"+randomStr
    print(key)
    url2 = "https://upload.qbox.me/"
    dict = {
        "token":token,
        "key":key
    }
    files = {"file":('账户资料上传的文件.jpg', open('C:/Users/1/PycharmProjects/feigua-houtai/file/账户资料上传的文件.jpg', 'rb'), 'image/jpg')}
    res = requests.post(url=url2,data=dict,files=files)
    r=res.json()
    fianl_url = r['url']
    print(fianl_url)
    return fianl_url
def test_manager_alter():
    url = "https://live-admin-qa1.youfenba.com/api/v1/manager/1099?"
    headers=test_headers()
    company = "test_测试公司",

    company_short="test_测试公司简称",
    logo=test_setup_function()
    remark='test备注',
    username='18230526256'
    company = "".join(list(company)),
    company_short = "".join(list(company_short)),
    remark ="".join(list(remark)),

    url = url + 'company'+'='+"".join(list(company))+'&'+'company_short'+'='+"".join(list(company_short))+'&'+'logo'+"="+logo+'&'+'remark'+'='+"".join(list(remark))+'&'+'username'+'='+username
    print(url)

    # dict={
    #     "company":"11111",
    #     "company_short":"22222",
    #     "logo": test_setup_function(),
    #     "remark":"test备注",
    #     "username":"18230526256"
    # }
    """图片未上传成功"""
    res = requests.put(url=url,headers=headers)
    r = res.json()
    assert r['company_short'] == company_short
    assert r['code'] == 200

