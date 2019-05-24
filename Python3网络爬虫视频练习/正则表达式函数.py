#-*-coding:utf-8-*-
__author__ = "Ink.white"

import re

#match 头部匹配
str1 = "poynkjapnynfipsalkjfyowrqmds"
pat1 = "oy.*"
print(re.match(pat1,str1))

#search
str2 = "poynkjapnynfipsalkjfyowrqmds"
pat2 = "oy.*"
print(re.search(pat2,str2))

#findall
str3 = "poynkjapnynfipsalkjfyowrqmds"
pat3 = "p.*?y"
print(re.compile(pat3).findall(str3))