#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import requests

files = {'files':open('favicon.ico','rb')}
r = requests.post('http://httpbin.org/post',files=files)
print(r.text)