# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/6 13:54
@Auth ： jiejia
@File ：test_update_coupon.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""批量修改F码"""
from tools.gettoken import test_headers
from tests.test_coupon_list import test_sech1
import requests
"""调用列表的查询接口"""
basic_url = "https://live-admin-qa1.youfenba.com"
headers=test_headers()
ids=test_sech1()
def test_updata_name():
    url = basic_url+"/api/v1/coupon/edit"
    dict={
        "ids":ids,
        "name":"自动批量修改测试",
        "type_discount":"11",
        "use_condition":"22",
        "channel_id":"",
        "channel_remark": "王杰佳修改",
        "count": 1,
    }
    res= requests.post(url=url,data=dict,headers=headers)
    r=res.json()
    assert r['code'] == 200





