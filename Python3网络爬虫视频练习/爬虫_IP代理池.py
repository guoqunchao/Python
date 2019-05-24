#_*_ coding:utf-8 _*_
__author__  = 'Ink.white'


import re
import urllib.request
import random

# ip = '68.13.196.233:8080'
ippools = [
    '68.13.196.233:8080',
    '68.13.196.233:8081',
]

def ip(ippools):
    thisIP = random.choice(ippools)
    print(thisIP)
    proxy = urllib.request.ProxyHandler({'http':thisIP})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

for i in range(0,3):
    try:
        ip(ippools)
        url = 'https://www.baidu.com'
        data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
        print(len(data))
        with open('E:\PycharmProjects\python爬虫系列\\ip_baidu_'+str(i)+'.html' ,'w') as f:
            f.write(data)
    except Exception as err:
        print(err)


