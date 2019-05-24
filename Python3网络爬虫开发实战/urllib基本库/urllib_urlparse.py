#_*_ coding:utf-8 _*_
__author__ = 'Inkwhite'

from urllib.parse import urlparse,urlsplit
result1 = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result1),result1)

# urlsplit和urlparse方法非常相似，只不过它不再单独解析params这一部分，只返回五个结果。
result2 = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result2),result2)

result3 = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
print(type(result2),result2)


result4 = urlparse('http://www.baidu.com/index.html;user?id=5#comment',allow_fragments=False)
print(result3.scheme,result3[0],result3.netloc,result3[1],sep='\n')

