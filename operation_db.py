__author__ = 'Xinrooy'
# -*- coding: utf-8 -*-
from condb import HY_condb
from Xinrooy_index import *
class HY_find(object):
    def HY_finddate(self,sql):
        connectdb = HY_condb()
        con = connectdb.HyCondb()
        cursor = con.connect.cursor()   #创建一个游标对象,python里的sql语句都要通过cursor来执行
        cursor.execute(sql)   #执行sql语句
        dbdate = cursor.fetchone() #读取查询结果
        cursor.close()
        connectdb.connect.close()
        return dbdate