# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'


import csv
with open("data.csv","r",encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

import pandas
df = pandas.read_csv('data1.csv')
print(df)