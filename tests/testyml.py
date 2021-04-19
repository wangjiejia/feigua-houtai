# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/6 20:27
@Auth ： jiejia
@File ：testyml.py
@IDE ：PyCharm
"""
import yaml
# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/6 16:19
@Auth ： jiejia
@File ：test_alluser.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""读取yaml文件"""
import pytest
import requests
import yaml
import os
# class readyaml(yamlpath):
#     @pytest.mark.datafile('C:/Users/1/PycharmProjects/feigua-houtai/tests/feigua-houtai.yml')
yamlPath="tests/feigua-houtai.yml"
def testyml():
    yamlPath = "C:/Users/1/PycharmProjects/feigua-houtai/tests/feigua-houtai.yml"
    print(yamlPath)
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % yamlPath)
    f = open(yamlPath,'r',encoding='utf-8')
    file_data = f.read()
    test_data = yaml.load(file_data)
    return test_data
if __name__=='__main__':
    testyml("feigua-houtai.yml")

