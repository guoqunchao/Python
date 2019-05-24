#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import requests

proxies = {
    "http":"http://127.0.0.1:1080/"
}

r = requests.get("http://en.ipip.net",proxies=proxies)
print(r.text)