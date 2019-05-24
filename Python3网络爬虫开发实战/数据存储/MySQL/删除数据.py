# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'

import pymysql

db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
cursor = db.cursor()
table = 'students'
condition = 'age < 22'
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
if cursor.execute(sql):
    print("Successful")
    db.commit()
else:
    print('Failed')
    db.rollback()
db.close()