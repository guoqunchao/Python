#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

from lxml import etree
text = '''
<li class="li-first"><a href="link.html">first item</a></li>
'''

html = etree.HTML(text)
result = html.xpath('//li[@class="li-first"]/a/text()')
print(result)

