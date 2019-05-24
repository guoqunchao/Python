#_*_ coding:utf-8 _*_
__author__ = "Ink.white"

import urllib.request

url = "http://blog.csdn.net"
headers =("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]

data = opener.open(url).read()
with open("E:\PycharmProjects\python爬虫系列\\a.html","wb") as f:
    f.write(data)