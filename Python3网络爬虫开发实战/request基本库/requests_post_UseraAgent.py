#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import requests

data = {'name':'Inkwhite'}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Host':'httpbin.org',
}
url = 'https://httpbin.org/post'

r = requests.post(url=url,data=data,headers=headers)
print(r.status_code)
print(r.text)