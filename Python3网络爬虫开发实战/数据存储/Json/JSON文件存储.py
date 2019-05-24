#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import json

str = \
[
    {
        "name":"Bob",
        "gender":"male",
        "birthday":"1992-10-18"
    },
    {
        "name":"肥花",
        "gender":"female",
        "birthday":"1995-10-18"
    }
]
with open("data.json","w") as f:
    f.write(json.dumps(str,indent=2,ensure_ascii=False))


with open("data.json","r") as v:
    data = json.loads(v.read())
    print(data)
    print(type(data))