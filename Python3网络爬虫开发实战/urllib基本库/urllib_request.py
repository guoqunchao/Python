__author__ = 'Ink.white'

import urllib.request

respose = urllib.request.urlopen('https://www.baidu.com')
print(respose.status)
print(respose.getheaders())
print(respose.getheader('Server'))

