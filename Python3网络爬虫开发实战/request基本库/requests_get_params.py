#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import requests

data = {
    'name':'germey',
    'age':22
}

r = requests.get('http://httpbin.org/get',params=data)
print(r.text)