#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import requests

# 将返回为JSON格式的转化为字典  如果不是JSON格式将报错
r = requests.get('http://httpbin.org/get')
print(r.text)
print(type(r.text))
print(r.json())
print(type(r.json()))




