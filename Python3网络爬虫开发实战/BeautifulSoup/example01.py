#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

from bs4 import BeautifulSoup

html = '''
<html>
<head><title>我的第一个 HTML 页面</title></head>
<body>
<p class="body" name="drmouse">body 元素的内容会显示在浏览器中。</p>
<p>title 元素的内容会显示在浏览器的标题栏中。</p>
</body>
</html>
'''

soup=BeautifulSoup(html,'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.title.name)
print(soup.p.attrs)
print(soup.p.attrs["name"])
print(soup.p['name'])
print(soup.p['class'])
print(soup.html.contents)

# 生成器的使用
text = ['a','b','c','d','e']
for i,v in enumerate(text):
    print(i,v)
print(list(enumerate(text,start=0)))
print(dict(enumerate(text,start=0)))
print(tuple(enumerate(text,start=0)))

print(soup.find_all(name='body'))