# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/22 17:33
@Auth ： jiejia
@File ：alluser_test.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import json
from itertools import count

import pytest
import allure
import requests
import yaml
import os
import requests
import json
"""区间比较的库"""
from interval import Interval
from tools.gettoken import test_headers
headers=test_headers()

class Request:
    def request(self,url,method='get',**kwargs):
        if method=='get':
            return requests.request(url=url,method=method,**kwargs)
        elif method=='post':
            return requests.request(url=url,method=method,**kwargs)
        elif method == 'put':
            return requests.request(url=url, method=method, **kwargs)
        elif method == 'delete':
            return requests.request(url=url, method=method, **kwargs)
    def get(self,url,**kwargs):
        return self.request(url=url,method='get',**kwargs)
    def post(self,url,**kwargs):
        return self.request(url=url,method='post',**kwargs)
    def put(self,url,**kwargs):
        return self.request(url=url,method='put',**kwargs)
    def delete(self,url,**kwargs):
        return self.request(url=url,method='delete',**kwargs)
# def readYaml():
#     with open('books.yaml','r') as f:
#         return list(yaml.safe_load_all(f))
# @pytest.mark.parametrize('datas',readYaml())
# def test_books(datas,headers):
#     if datas['method']=='get':
#         r=Request().get(url=datas['url'],headers=headers)
#         assert  datas['expect'] in json.dumps(r.json(),ensure_ascii=False)
#     elif datas['method'] == 'post':
#         r = Request().post(url=datas['url'], json=datas['dict1'], headers=headers)
#         assert datas['expect'] in json.dumps(r.json(), ensure_ascii=False)
#     elif datas['method'] == 'put':
#         r = Request().put(url=datas['url'], json=datas['dict1'], headers=headers)
#         assert datas['expect'] in json.dumps(r.json(), ensure_ascii=False)
#     elif datas['method'] == 'delete':
#         r = Request().delete(url=datas['url'], headers=headers)
#         assert datas['expect'] in json.dumps(r.json(), ensure_ascii=False)
# def test_alluser(headers):
#     url="https://live-admin-qa1.youfenba.com/api/v1/manager?page=1&limit=50"
#     r=Request().get(url=url,headers=headers)
#     print(headers)
#     print(url)
#     assert r.json()
"""申明了fixture，就可以将被申明的fixture，整个函数都用作参数进行调用"""
@pytest.fixture()
def test_alluser(headers):
    url="https://live-admin-qa1.youfenba.com/api/v1/manager?page=1&limit=50"
    # data = {'username':'admin','password':'123123'}
    r=requests.get(url=url,headers=headers)
    req=r.json()
    print(req)
    return req
def test1_code(test_alluser):
    req = test_alluser
    req['code'] == 200
@allure.feature('用户名查询')
def test_username(headers):
    url = "https://live-admin-qa1.youfenba.com/api/v1/manager?username=18230526256&page=1&limit=50"
    r=requests.get(url=url,headers=headers)
    req=r.json()
    print(req)
    assert req['code'] == 200
    assert ((((req['data'])['list'])[0]))['username'] == '18230526256'
    assert (len((req['data'])['list'])) == 1
    """len()函数计算返回中数据的个数"""
    return req
@allure.feature('公司名称查询')
def test_company(headers):
    url="https://live-admin-qa1.youfenba.com/api/v1/manager?name=&company=%E9%87%8D%E5%9C%A8%E9%81%87%E7%9F%A5%E5%B7%B1&page=1&limit=50"
    r=requests.get(url=url,headers=headers)
    req=r.json()
    assert  ((((req['data'])['list'])[0])['company']) == "山河不足重"
@allure.feature('抖音号查询')
def test_douyin(headers):
    url="https://live-admin-qa1.youfenba.com/api/v1/manager?name=&company=&uid=%E9%A3%9E%E7%93%9C%E6%99%BA%E6%8A%95%E8%BF%90%E8%90%A5%E5%8F%B7&page=1&limit=50"
    r = requests.get(url=url, headers=headers)
    req = r.json()
    assert (((((req['data'])['list'])[0])['last_douyin']))['nickname'] == '飞瓜智投运营号'
@allure.feature('渠道查询')
def test_channel(headers):
    url="https://live-admin-qa1.youfenba.com/api/v1/manager?name=&company=&uid=&channel_id=96&page=1&limit=50"
    r = requests.get(url=url, headers=headers)
    req = r.json()
    assert (((((req['data'])['list'])[0])))['channel_id'] == 96
    assert (((((req['data'])['list'])[0])['channel']))['name'] == '官网H5'
@allure.feature('绑定微信名称查询')
def test_weixinname(headers):
    url="https://live-admin-qa1.youfenba.com/api/v1/manager?name=&company=&uid=&wx_nickname=%E9%99%88%E5%90%8C%E5%AD%A6&page=1&limit=50"
    r = requests.get(url=url, headers=headers)
    req = r.json()
    assert ((((((req['data'])['list'])[0])['weixin']))[0])['nickname'] == '陈同学 | 面朝'
@allure.feature('是否开通自动录播查询')
def test_auto(headers):
    url="https://live-admin-qa1.youfenba.com/api/v1/manager?name=&company=&uid=&wx_nickname=&auto_record=1&page=1&limit=50"
    r = requests.get(url=url, headers=headers)
    req = r.json()
    assert (((((req['data'])['list'])[0])['auto_record']))['auto_record'] == 1
@allure.feature('用户类型查询')
def test_type(headers):
    url="https://live-admin-qa1.youfenba.com/api/v1/manager?name=&company=&uid=&wx_nickname=&type=0&page=1&limit=50"
    r = requests.get(url=url, headers=headers)
    req = r.json()
    assert (((((req['data'])['list'])[0])['type'])) == 0
@allure.feature('是否是超级会员查询')
def test_isvip(headers):
    url="https://live-admin-qa1.youfenba.com/api/v1/manager?name=&company=&uid=&wx_nickname=&is_vip=1&page=1&limit=50"
    r = requests.get(url=url, headers=headers)
    req = r.json()
    assert (((((req['data'])['list'])[0])['is_vip'])) == 1
@allure.feature('创建时间查询')
def test_createtime(headers):
    url="https://live-admin-qa1.youfenba.com/api/v1/manager?name=&company=&uid=&wx_nickname=&start_at=2021-03-24&end_at=2021-03-25&page=1&limit=50"
    r = requests.get(url=url, headers=headers)
    req = r.json()
    a= Interval('2021-03-25 00:00:00','2021-03-26  00:00:00')
    assert ((((req['data'])['list']))[0])['created_at']  in  a
@allure.feature('过期时间查询')
def test_expiredtime(headers):
    url="https://live-admin-qa1.youfenba.com/api/v1/manager?name=&c ompany=&uid=&wx_nickname=&expired_start_at=2021-03-01&expired_end_at=2021-03-29&page=1&limit=50"
    r = requests.get(url=url, headers=headers)
    req = r.json()
    b= Interval('2021-03-01 00:00:00','2021-03-29  00:00:00')
    assert ((((req['data'])['list']))[0])['expired_at']  in b
@pytest.mark.flaky(reruns=5)
@allure.feature('全部用户列表所有筛选项一起查询')
def test_allsearch(headers):
    url="https://live-admin-qa1.youfenba.com/api/v1/manager?name=18230526256&company=%E9%87%8D%E5%9C%A8%E9%81%87%E7%9F%A5%E5%B7%B1&uid=%E9%A3%9E%E7%93%9C%E6%99%BA%E6%8A%95%E8%BF%90%E8%90%A5%E5%8F%B7&wx_nickname=%E6%88%91%E8%A6%81%E5%87%BA%E9%97%A8%E6%89%94%E4%B8%AA%E5%9E%83%E5%9C%BE&auto_record=1&type=1&is_vip=1&start_at=2021-03-15&end_at=2021-03-31&expired_start_at=2021-04-01&expired_end_at=2021-04-30&channel_id=96&page=1&limit=50"
    r = requests.get(url=url, headers=headers)
    req = r.json()
    c = Interval('2021-03-15 00:00:00', '2021-03-31  00:00:00')
    d = Interval('2021-03-01 00:00:00', '2021-04-20  00:00:00')
    assert req['code'] == 200
    assert ((((req['data'])['list'])[0]))['username'] == '18230526256'
    assert (len((req['data'])['list'])) == 1
    assert ((((req['data'])['list'])[0])['company']) == "山河不足"
    assert (((((req['data'])['list'])[0])['last_douyin']))['nickname'] == '飞瓜智投运营号'
    assert (((((req['data'])['list'])[0])))['channel_id'] == 9
    assert (((((req['data'])['list'])[0])['channel']))['name'] == '官网H5'
    assert ((((((req['data'])['list'])[0])['weixin']))[0])['nickname'] == '我要出门扔个垃圾'
    assert (((((req['data'])['list'])[0])['auto_record']))['auto_record'] == 1
    assert (((((req['data'])['list'])[0])['type'])) == 1
    assert (((((req['data'])['list'])[0])['is_vip'])) == 1
    assert ((((req['data'])['list']))[0])['created_at'] in c
    assert ((((req['data'])['list']))[0])['expired_at'] in d

# if __name__ == '__main__':
#     """os.path.dirname(__file__) 返回脚本的路径"""
#     pytest.main(['user_test.py','--alluredir','./report/allure'])
#     os.system('allure serve report/allure')
#     # path=os.path.dirname(__file__)
#     # print(path)
#     # path=path + "/report/"
#     # pytest.main(['-s','-q','--allured',path])
#     #















