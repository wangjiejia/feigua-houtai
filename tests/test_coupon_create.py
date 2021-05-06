# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/30 17:30
@Auth ： jiejia
@File ：coupon.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""生成F码"""
import requests
from tools.gettoken import test_headers
headers=test_headers()

url="https://live-admin-qa1.youfenba.com/api/v1/coupon"
def test_coupon_create_nameisnull():
    dict={
        "channel_id":98,
        "count": 1,
        "name": "测试工作",
        "type": 1,
        "type_discount": 11100,
        "use_condition": 100
    }
    res = requests.post(url=url,data=dict,headers=headers)
    r=res.json()
    print(r)
#     assert r['message'] == "请输入优惠券名称"
# """测试测试"""
# def test_coupon_create_discountisnull():
#     dict={
#         "name": "接口测试测试",
#         "type_discount": 11,
#         "use_condition": 100,
#         "channel_id": 98,
#         "channel_remark": "测试测试测试测试测手册",
#         "count": 1,
#         "type": 1,
#     }
#     res = requests.post(url=url,data=dict,headers=headers)
#     r=res.json()
#     print(r)
#     # assert r['message'] == "请输入优惠券名称"
