#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import requests
# data = {'name':'Inkwhite','age':22}
# r = requests.post('http://httpbin.org/post',data=data)
# print(r.text)


s = requests.get('http://www.baidu.com')
print(s.status_code)
exit() if not s.status_code == requests.codes.ok else print('Request Successfully!')