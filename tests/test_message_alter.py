# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/30 11:52
@Auth ： jiejia
@File ：test_message_alter.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from tools.gettoken import test_headers
headers=test_headers()
def test_message_alter1():
    account_limit= 1,
    add_order= "1",
    buy_limit= 1,
    expired_at="2021-04-30",
    is_vip= "1",
    order_type= "2",
    pay_price= 9900,
    pay_type= "alipay",
    price= 10000,
    type= "10",
    url = "https://live-admin-qa1.youfenba.com/api/v1/vip/1099?"
    url = url + 'account_limit' + '=' + "".join(str(account_limit)) + '&' + 'add_order' + '=' + "".join(
        list(add_order)) + '&' + 'buy_limit' + "=" + str(buy_limit)+ '&' + 'expired_at' + '=' + "".join(
        list(expired_at)) + '&' + 'is_vip' + '=' +str(is_vip)+ '&' + 'order_type' + '=' + str(order_type)+ '&' + 'pay_price' + '=' +  str(pay_price)+ '&' + 'pay_type' + '=' +  str(pay_type)+ '&' + 'price' + '=' +  str(price)+ '&' + 'type' + '=' +  str(type)
    print(url)
    # url = url + 'account_limit'+'='+"".join(list(account_limit))+'&'+'company_short'+'='+"".join(list(company_short))+'&'+'logo'+"="+logo+'&'+'remark'+'='+"".join(list(remark))+'&'+'username'+'='+username
    # # print(url)
    # headers=test_headers()
    #
    #
    # res=requests.put(url=url,data=dict,headers=headers)
    # r = res.json()
    # print(r)


