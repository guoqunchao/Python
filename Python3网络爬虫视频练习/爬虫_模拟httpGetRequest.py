#_*_ coding:utf-8 _*_
__author__ = "Ink.white"

import urllib.request
import re

kw = "apple"
kw = urllib.request.quote(kw)
for i in range(1,11):
    url = "https://www.baidu.com/s?wd="+kw+"&pn="+str((i-1)*10)
    pat1 = "'title':'(.*?)',"
    pat2 = '"title":"(.*?)",'
    data = urllib.request.urlopen(url).read().decode("utf-8")

    result1 = re.compile(pat1).findall(data)
    result2 = re.compile(pat2).findall(data)
    for z in range(0,len(result1)):
        print(result1[z])

    for x in range(0,len(result2)):
        print(result2[x])