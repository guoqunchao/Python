#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

# URL初始化

from pyquery import PyQuery
doc = PyQuery(url='https://cuiqingcai.com')
# doc = PyQuery(requests.get('https://cuiqingcai.com').text)
print(doc('title'))


