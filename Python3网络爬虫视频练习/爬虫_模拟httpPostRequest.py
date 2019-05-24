#_*_ conding:utf-8 _*_
__author__ = "Ink.white"

import urllib.request
import urllib.parse

postUrl = "http://iqianyue.com/mypost"
postData = urllib.parse.urlencode({
    "name":"guoqunchao@abc.com",
    "pass":"aslujxlkvjoiw"
}).encode("utf-8")

obj = urllib.request.Request(postUrl,postData)
result = urllib.request.urlopen(obj).read().decode("utf-8")

print(result)