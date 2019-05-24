#-*- coding:utf-8 -*-

__author__ = 'Ink.White'


from pyquery import PyQuery

html = '''
<html>
<head><title>我的第一个 HTML 页面</title></head>
<body>
<div id="container">
    <a class="body">
        <p name="drmouse">body 元素的内容会显示在浏览器中。</p>
        <p>title 元素的内容会显示在浏览器的标题栏中。</p>
    </a>
</div>
</body>
</html>
'''

doc = PyQuery(html)
print(doc("#container .body p"))