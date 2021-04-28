# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/1 16:02
@Auth ： jiejia
@File ：work.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# -*- coding: utf-8 -*-
"""根据当前的方法名称进行判断，方法名称与yml文件中的测试名称相同时，则请求接口 """

import requests
from tests.testyml import testyml
from tools.gettoken import test_headers
headers = test_headers()
class Test_get_yml_data():
    def test_get_yml(self,name):
        self.name = name
        """获取到当前方法名称"""
        """获取到yml文件中的数据"""
        test_new_data = testyml()
        list_count = len(test_new_data)
        for i in range(0, list_count):
            test_second_data = test_new_data[i]
            test_name = (test_second_data['test'])['name']
            if name == test_name:
                for yaml_case in test_second_data:
                    method = (test_second_data['test'])['method']
                    url_data = (test_second_data['test'])['url']
                    json = (test_second_data['test'])['json']
                    extract = (test_second_data['test'])['extract']
                    if method == 'GET':
                        res = requests.get(url=url_data, params=json, headers=headers)
                        r = res.json()

                        return r
                    elif method == 'POST':
                        res = requests.post(url=url_data, params=json, headers=headers)
                        r = res.json()

                        return r
                        # assert (r['code']) == extract
                    elif method == 'PUT':
                        res = requests.put(url=url_data, params=json, headers=headers)
                        r = res.json()

                        return r
                        # assert (r['code']) == extract
                    else:
                        res = requests.delete(url=url_data, params=json, headers=headers)
                        r = res.json()

                        return r
                        # assert (r['code']) == extract
                        break




x = Test_get_yml_data()


























