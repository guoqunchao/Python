# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'

import pymysql

db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >21'
# try:
#     cursor.execute(sql)
#     print("Cont:",cursor.rowcount)
#     # one = cursor.fetchone()
#     # print(one)
#     all = cursor.fetchall()
#     print(all)
#     print(type(all))
#     for i in all:
#         print(i)
# except:
#     print('Error')

print('# while循环遍历 fetchall取数据量大会占用非常高的开销')
try:
    cursor.execute(sql)
    print("Cont:",cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print("Row:",row)
        row = cursor.fetchone()
except:
    print("Error")