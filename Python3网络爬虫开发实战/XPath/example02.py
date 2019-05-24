#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

from lxml import etree

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''

# 通过contains()方法匹配 只要包含此属性就可
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li-first")]/a/text()')
print(result)