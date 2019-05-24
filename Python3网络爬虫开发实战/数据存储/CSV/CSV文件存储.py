# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'

import csv


with open('data.csv','w',encoding='utf-8',newline='') as f1:
    writer1 = csv.writer(f1)
    writer1.writerow(['id','name','age'])
    # writer1.writerow(['10001','Mike',20])
    # writer1.writerow(['10002','Baob',22])
    # writer1.writerow(['10003','Jack',12])
    writer1.writerows([['10001','Mike',20],['10003','Jack',12],['10002','Baob',22]])  #等同于上面三条，writerows写入多行


with open('data1.csv','w',encoding='utf-8',newline='') as f2:
    fieldnames = ['id','name','age']
    writer2 = csv.DictWriter(f2,fieldnames=fieldnames)
    writer2.writeheader()
    writer2.writerow({'id':'1001','name':'Mike','age':22})
    writer2.writerow({'id':'1002','name':'Bobe','age':23})
    writer2.writerow({'id':'1003','name':'Joan','age':24})

