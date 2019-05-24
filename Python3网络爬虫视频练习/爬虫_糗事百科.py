#_*_ coding:utf-8 _*_
__author__ = "Ink.white"

import urllib.request
import re

header = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [header]
urllib.request.install_opener(opener) # 安装全局头

#<a class="recmd-content" href="/article/121152471" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">就问你舒服不舒服！</a>
pat = '<a class="recmd-content" href=.*?target="_blank".*?>(.*?)</a>'
for i in range(0,30):
    url = 'https://www.qiushibaike.com/8hr/page/'+str(i+1)+"/"
    data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
    thisdata = re.compile(pat,re.S).findall(data)
    for j in range(0,len(thisdata)):
        print(thisdata[j])
        print('-------------------')

