#-*- coding:utf-8 -*-
__author__ = "Ink.white"

import urllib.request
import re

obj = urllib.request.urlopen("https://read.douban.com/provider/all").read().decode()
pat = '<div class="name">(.*?)</div>'
rst = re.compile(pat).findall(obj)

print(rst)
with open("info.py","w") as f:
    for i in range(0,len(rst)):
        f.write(rst[i])
