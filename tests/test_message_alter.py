# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/30 14:59
@Auth ： jiejia
@File ：test_message_alter.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""修改用户会员信息"""
from tools.gettoken import test_headers
import requests
from tools.conndata import Test_DButil
data_sql=Test_DButil()
import datetime
def test_message_alter():
    account_limit=  "1"
    add_order=  "1"
    buy_limit=  "1"
    expired_at=  "2021-04-30"
    is_vip=  "1"
    order_type=  "2"
    pay_price=  "9900"
    pay_type=  "alipay"
    price=  "10000"
    type=  "10"
    url1 = "https://live-admin-qa1.youfenba.com/api/v1/manager/1099?"
    url = url1 + 'account_limit'+'='+"".join(tuple(account_limit))+'&'+'add_order'+'='+"".join(tuple(add_order))+'&'+\
          'buy_limit'+"="+"".join(tuple(buy_limit))+'&'+'expired_at'+'='+"".join(tuple(expired_at))+'&'+\
          'is_vip'+'='+"".join(tuple(is_vip))+'&'+'order_type'+'='+"".join(tuple(order_type))+'&'+\
          'pay_price'+"="+"".join(tuple(pay_price))+'&'+'pay_type'+'='+"".join(tuple(pay_type))+\
          '&'+'price'+'='+"".join(tuple(price))+'&'+'type'+'='+"".join(tuple(type))
    headers = test_headers()
    res = requests.put(url=url,headers=headers)
    r = res.json()
    cur = datetime.datetime.now()
    time = str(datetime.datetime.strptime(cur,'%b %d %Y')).split(' ')[3]
    print(time)

    # user_id = data_sql.test_selectsingle(field="*", table="vip_order", where="user_id" + "=" + "'" + "1099" + "'"+ 'and' +" " + "created_at" + "="+ "'"+ str(cur) +"'" )
    # print(user_id)
    # assert (r['data'])['id'] == 1099
    # assert r['code'] == 200
    # print(r)





