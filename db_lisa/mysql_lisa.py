# -*- coding: UTF-8 -*-
import pymysql as mdb



def mysql_lisa(config):
    def __init__(self):
        self.conn = mdb.connect(**config)
        self.cursor = self.conn.cursor()
    # 创建数据库

    # 创建表



    # 查询数据

    # 查询数据条目

    # 查询数据

    # 更新记录

    # 删除记录

    # 初始化
    def __init__(self):
        self.conn = mdb.connect(**config)
        self.cursor = self.conn.cursor()

    # 批量插入数据，数据为列表
    def insert(self,sql,values):
         self.cursor.executemany(sql, values)

    # 插入单条数据，数据为列表
    def insert(self,sql,values):
        for v in values:
            self.cursor.execute('INSERT INTO test values(%s,%s)', v)

    # 查询数据
    def query(self, sql):
        """  Execute SQL statement """
        return self.cursor.execute(sql)

    def show(self):
        """ Return the results after executing SQL statement """
        return self.cursor.fetchall()

    # 注销
    def __del__(self):
        """ Terminate the connection """
        self.conn.close()
        self.cursor.close()









config = {
    'host': '192.168.1.213',
    'port': 3306,
    'user': 'exchange',
    'passwd': 'hip7Ae8k',
    'db': 'exchange',
    'charset': 'utf8'
}