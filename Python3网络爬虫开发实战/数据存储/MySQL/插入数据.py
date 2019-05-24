# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'

import pymysql

id = '20120001'
name = 'Bob'
age = 20

db = pymysql.connect(host='localhost',user='root',password='123456',db='spiders',port=3306)
cursor = db.cursor()
sql = 'INSERT INTO students(id,name,age) values (%s,%s,%s)'
try:
    cursor.execute(sql,(id,name,age))
    db.commit()
except:
    db.rollback()
db.close()


'''
事务操作标准写法
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
'''

