#-*- coding:utf-8 -*-

__author__ = 'Ink.White'


from requests import Request,Session

url = 'http://httpbin.org/post'
data = {
    'name':'inkwhite'
}
headers = {
    'User-Agebt':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

s = Session()
req = Request('POST',url=url,data=data,headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)