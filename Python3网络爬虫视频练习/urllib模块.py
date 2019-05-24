#-*- coding:utf-8 -*-
__author__ = "Ink.white"

import urllib.request
import json

'''
# 去网址内容到本地文件（网址，本地文件存储位置)
urllib.request.urlretrieve("https://www.baidu.com","E:\PycharmProjects\python爬虫系列\\download.html")

# 清除缓存
urllib.request.urlcleanup()

# 看网页相应简介信息
file = urllib.request.urlopen("https://www.baidu.com")
print(file.info())

# 获取状态码
print(file.getcode())

# 获取当前访问的网页url
print(file.geturl())
'''

# 超时设置
for i in range(1,100):
    try:
        file1 = urllib.request.urlopen("https://www.baidu.com",timeout=1)
        print(len(file1.read().decode("utf-8")))
    except Exception as err:
        print("出现异常" +str(err))
