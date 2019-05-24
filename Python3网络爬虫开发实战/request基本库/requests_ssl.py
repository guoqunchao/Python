#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import requests

r = requests.get("https://gitlab.dev.zichan360.com",verify=False)
print(r.status_code)


'''设置忽略警告的方式'''
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
r1 = requests.get("https://gitlab.dev.zichan360.com",verify=False)
print(r1.status_code)


'''通过捕获警告到日志的方式忽略警告'''
import logging
import requests

logging.captureWarnings(True)
r2 = requests.get("https://gitlab.dev.zichan360.com",verify=False)
print(r2.status_code)
