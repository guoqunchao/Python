#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'
}
r = requests.get('http://www.zhihu.com/explore',headers=headers)
title = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S).findall(r.text)
print(title)


print('-------------------------------------------')
r2 = requests.get('https://github.com/favicon.ico')
print(r2.text)    # 图片音频和视频这些文件本质上是二进制码组成
print(r2.content)
with open('favicon.ico','wb') as f:
    f.write(r2.content)