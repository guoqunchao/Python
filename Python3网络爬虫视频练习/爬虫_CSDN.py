#_*_ coding:utf-8 _*_
__author__ = "Ink.white"

import urllib.request
import re

url = "https://blog.csdn.net/"
header = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [header]
urllib.request.install_opener(opener)

data = urllib.request.urlopen(url).read().decode('utf-8')
print("首页数据大小：",len(data))
pat = '<h2>.*?<a href="(.*?)" target="_blank".*?data-track-click.*?</h2>'
thisLink = re.compile(pat,re.S).findall(data)
print("需爬取的链接：",thisLink)
print("需爬取的链接长度：",len(thisLink))

for i in range(0,len(thisLink)):
    urllib.request.urlretrieve(thisLink[i],"E:\\PycharmProjects\\python爬虫系列\\csdn_content\\"+str(i)+".html")
    print("当前文章(第"+str(i)+"篇)爬取成功！")
