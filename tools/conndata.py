# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/30 16:18
@Auth ： jiejia
@File ：pymsql_data.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""连接数据库"""
import pymysql
import pytest
from pymysql import cursors
"""连接数据库"""
class Test_DButil(object):
    config = {
        "host": "118.178.114.233",
        "username": "root",
        "passwd": "AyoufenbBwoca123",
        "database": "douyin_livetools",
        "charset": "gbk",
        "port": 31445
    }
    # print(config['username'])
    """连接数据库，连接成功则返回link ok ；连接失败则返回 not link"""
    def test_link_mysql(self):
        self.host = self.config['host']
        self.port = int(self.config['port'])
        self.user = self.config['username']
        self.passwd = self.config['passwd']
        self.db = self.config['database']
        self.charset = self.config['charset']
        print(self.port)
        try:
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db,charset=self.charset
            )
            self.cursor = self.conn.cursor()
            data = "link ok"
            print(data)
            return self.conn
        except:
            print('connect mysql error')

        # print(self.config['username'])
        """执行数据库语句，执行失败则报错"""
    # def test_query_data(self,sql):
    #     self.cursor.execute(sql)
    #     rowcount = self.cursor.rowcount
    #     return rowcount
    """查询数据"""
    """单个条件查询"""
    def test_selectsingle(self,**kwargs):
        x = Test_DButil.test_link_mysql(self)
        table = kwargs['table']
        table = 'table' in kwargs and kwargs['table'] or '*'
        field = 'field' in kwargs and kwargs['field'] or '*'
        where = 'where' in kwargs and 'where' + ' ' + kwargs['where'] or '*'
        order = 'order' in kwargs and 'order by' + kwargs['order'] or '*'
        sql = "select %s from %s %s" % (field, table, where)
        # sql = 'select * from manager where username = "18682491020"'
        print(sql)
        # sql = kwargs['sql']
        self.cursor.execute(sql)
        # Test_DButil.test_query_data(self,sql=sql)
        try:
            # self.cursor.execute(sql)
            data = self.cursor.fetchone()
            return data
        except:
            self.conn.rollback()
    # """多个条件查询"""
    # def test_selectall(self,**kwargs):
    #     table = 'table' in kwargs and kwargs['table'] or '*'
    #     field = 'field' in kwargs and kwargs['field'] or '*'
    #     where ='where' in kwargs and kwargs['where'] or '*'
    #     order ='order' in kwargs and kwargs['order'] or '*'
    #     sql = 'select %s from %s where %s and %s'%(field,table,where,order)
    #     print(sql)
    #     self.cursor.execute(sql)
    #     try:
    #         data = self.cursor.fetchone()
    #         return data
    #     except:
    #         self.conn.rollback()
        """删除数据"""
    def test_delete(self,**kwargs):
        # delect from manager where username = ""
        table = 'table' in kwargs and kwargs['table'] or '*'
        field = 'field' in kwargs and kwargs['field'] or '*'
        where = 'where' in kwargs and kwargs['where']
        sql1 = 'delete from %s where %s'%(table,field)
        print(sql1)
        x = self.cursor.execute(sql1)
        self.conn.commit()





