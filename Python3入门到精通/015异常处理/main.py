# -*- coding:utf-8 -*-

'''
try:
    pass  #检测范围
except expression as identifier:
    pass #出现异常后的处理代码
'''


try:
    with open("file.txt") as f:
        print(f.read())
except OSError as identifier:
    print('文件异常:' + str(identifier))
except TypeError as identifier:
    print('文件异常:' + str(identifier))



'''
try:
    pass #检测范围
except expression as identifier:
    pass #出现异常后的处理代码
finally:
    pass #无论如何都会被执行的代码
'''

