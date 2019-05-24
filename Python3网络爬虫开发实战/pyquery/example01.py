# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'

# 字符串初始化

html = '''
<html>
<head><title>我的第一个 HTML 页面</title></head>
<body>
<p class="body" name="drmouse">body 元素的内容会显示在浏览器中。</p>
<p>title 元素的内容会显示在浏览器的标题栏中。</p>
</body>
</html>
'''

from pyquery import PyQuery
doc = PyQuery(html)
print(doc('p'))

