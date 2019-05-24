#-*-conding:utf-8-*-
__author__ = "Ink.white"

import re

print("#原子表")
#普通字符做原子
str = "pythonproject"
pat = "pro"
print(re.search(pat,str))


#非打印字符做原子
str1 = """
pythondezheng
zebiaodashi
"""
pat1 = "\n"
print(re.search(pat1,str1))

"""
\w 匹配字母、数字、下划线
\W 匹配非字母、数字、下划线
\d 匹配数字(十进制数)
\D 匹配非数字(十进制数)
\s 匹配空白字符
\S 匹配非空白字符
"""
str2 = "lkjaskdj1092093rlkasjflk"
pat2 = "\w\d\d"
print(re.search(pat2,str2))


str3 = "taoyunnnn128974980sdfs"
pat3 = "tao[xyz]"
# pat3 = "tao[^xyz]"  #^非xyz
print(re.search(pat3,str3))


print("\n#元字符")
"""
元字符
. 除换行外任意一个字符
^ 开始位置
$ 结束位置
* \0\1\多次
？ \0\1
+ \1\多次
{n} 恰好n次
{n,} 至少n次
{n.m} 至少n次，至多m次
| 或
() 模式单元
"""
str4 = "taoyunnnn128974980sdfs"
pat4 = "(n|a){3,}"
print(re.search(pat4,str4))

print("\n#模式修正符")
#模式修正符
"""
I 匹配时忽略大小写
M 多行匹配*
L 本地化识别匹配
U unicode
S 让.匹配包括换行符
"""
str5 = "Python"
pat5 ="pyt"
print(re.search(pat5,str5,re.I))

print("\n#贪婪模式与懒惰模式")
str6 = "poythony"
# pat6 = "p.*y"
pat6 = "p.*?y"
print(re.search(pat6,str6))

str7 = "<a href='https://www.baidu.com'>百度知道</a>"
pat7 = "[a-zA-Z]*://[^\s]*[com|cn]"
print(re.compile(pat7).findall(str7))

str8 = "jjksajfla021-1098502938501lakjiojqqw0487-1209482104125k32ewlsdv"
pat8 = "\d{4}-\d{7}|\d{3}-\d{8}"
print(re.compile(pat8).findall(str8))











