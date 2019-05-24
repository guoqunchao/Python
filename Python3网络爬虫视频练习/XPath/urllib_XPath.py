# -*- coding:utf-8 -*-

__author__ = 'Ink.white'

import re
import urllib.request
from lxml import etree
import random
from useragent import *

userAgent(uapools)

data = urllib.request.urlopen('https://www.baidu.com').read().decode('utf-8','ignore')
print(data)
treedata = etree.HTML(data)
title = treedata.xpath("//title/text()")
print(title)
print(type(title))

if(str(type(title)) == "<class 'list'>"):
    pass
else:
    title = [i for i in title]