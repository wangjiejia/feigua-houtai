# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/1 17:14
@Auth ： jiejia
@File ：connmysql.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import pymysql.cursors
import pytest
class Test_sql(object):
    config = {
        "host": "118.178.114.233",
        "username": "root",
        "passwd": "AyoufenbBwoca123",
        "database": "douyin_livetools",
        "charset": "gbk",
        "port": 31445
    }
    def open(self):
        self.host = self.config['host']
        self.port = int(self.config['port'])
        self.user = self.config['username']
        self.passwd = self.config['passwd']
        self.database = self.config['database']
        self.charset = self.config['charset']
        try:
            self.db = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.database,
                                        charset=self.charset)
            print("link ok")
        except:
            print("error")


        # self.table = "manager"
        # sql = "select * from" + " " + self.table
        self.cur = self.db.cursor()
        """数据库关闭方法"""
    def close(self):
        self.cur.close()
        self.db.close()
    """数据库执行操作方法"""
    def exe(self,sql,L=[]):
        self.sql=sql
        try:
            self.open()
            self.cur.execute(sql,L)
            self.db.commit()
            print("OK")
        except Exception as e:
            self.db.rollback()
            print("Failed",e)







        #
        # self.cur = self.db.cursor()
        # result = cursor.execute(sql)
        # self.conn.commit()
        # print(result)

        # try:
            # self.cursor = self.conn.cursor()
            # self.cursor.execute(sql)
            # row = self.cursor.fetchone()
            # print(row)
        # except:
        #     print(sql + 'execute failed.')
    #
    # def open(self):
    #     pass


if __name__=='__main__':
    pytest.main(['connmysql.py'])

