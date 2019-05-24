# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'

import pymysql

data = {
    'id':'20120004',
    'name':'Jack',
    'age':29
}
db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
cursor = db.cursor()
tables = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s']*len(data))
sql = 'INSERT INTO {tables}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE'.format(tables=tables,keys=keys,values=values)
update = ', '.join([" {key} = %s".format(key=key) for key in data])
sql +=update
print(sql)

if cursor.execute(sql,tuple(data.values())*2):
    print("Successful")
    db.commit()
else:
    print('Failed')
    db.rollback()
db.close()
