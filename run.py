# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/30 10:50
@Auth ： jiejia
@File ：run.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""执行测试用例"""
import pytest
import os
import allure
if __name__=='__main__':
    """此时生成的报告文件为json格式"""
    # pytest.main(["-s", "--alluredir", "生成报告路径", "执行的测试文件"])
    pytest.main(["-s","alluredir","./report","gettoken.py"])
    # pytest.main(["-s","--alluredir","./report","user_test.py"])
    """将json格式转换成html格式"""
    os.system('allure generate ./report/ -o ./report/html/ --clean')
    """右键使用浏览器打开正确，直接复制出去打开失败；可先通过本地渲染，再进行打开"""
    os.system("allure open ./report/html/")




