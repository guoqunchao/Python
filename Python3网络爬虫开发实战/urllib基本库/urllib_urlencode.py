__author__ = 'Inkwhite'

from urllib.parse import urlencode
# 序列化 urlencode将设定好的字典格式转化为GET请求参数
params = {
    'name':'中国',
    'age':22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)


# 反序列化 GET请求转化字典
from urllib.parse import parse_qs
query = 'name=germey&age=22'
print(parse_qs(query))


# GET请求解析为元组组成的列表
from urllib.parse import parse_qsl
query1 = 'name=germey&age=22'
print(parse_qsl(query1))