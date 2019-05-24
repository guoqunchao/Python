# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'

from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy = '127.0.0.1:1080'
proxy_handle = ProxyHandler({
    'http':'http://' + proxy,
    'https':'https://' + proxy
})

opener = build_opener(proxy_handle)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)