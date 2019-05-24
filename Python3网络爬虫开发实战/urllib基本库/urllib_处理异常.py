# -*- coding:utf-8 -*-
__author__ = 'Ink.white'

from useragent import *
userAgent(uapools)
from urllib import request,error

try:
    response =request.urlopen('https://cuiqingcai.com/index.htm')
    # response =request.urlopen('https://www.baidu.com')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print("Request Successfully!")