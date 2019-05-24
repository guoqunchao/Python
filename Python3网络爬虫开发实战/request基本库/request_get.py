#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import requests

r = requests.get('https://www.baidu.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

print('-------------------------------------------')
s = requests.get('http://httpbin.org/get')
print(s.text)