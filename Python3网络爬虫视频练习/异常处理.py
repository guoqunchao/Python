#_*_ coding:utf-8 _*_
__author__ = "ink.white"

import urllib.request
import urllib.error

try:
    urllib.request.urlopen("http://blog.csdn.net/deasfaf/")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)