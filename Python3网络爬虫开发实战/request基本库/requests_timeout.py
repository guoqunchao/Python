#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import requests

r = requests.get('http://www.taobao.com',timeout=1)
print(r.text)