#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import requests

r = requests.get('http://localhost:5000',auth=('username','password'))
print(r.status_code)