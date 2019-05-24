#-*- coding:utf-8 -*-

__author__ = 'Ink.White'


import requests

requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)

print('''-------------------------------------''')

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r1 = s.get('http://httpbin.org/cookies')
print(r1.text)
print(type(r1))
print(r1.json())
print(type(r1.json()))