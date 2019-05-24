#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

'''
\w    配字母、数字及下划线
\W    配不是字母、数字及下划线的字符
\s    配任意空白字符，等价于[\t\n\r\f]
\S    配任意非空字符
\d    配任意数字，等价于[0-9]
\D    配任意非数字的字符
\A    配字符串开头
\Z    配字符串结尾，如果存在换行，只匹配到换行钱的结束字符串
\z    配字符串结尾，如果存在换行，同时还会匹配换行符
\G    配最后匹配完成的位置
\n    配一个换行符
\t    配一个制表符
^     配一行字符串的开头
$     配一行字符串的结尾
.     配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
[...] 用来表示一组字符，单独列出，比如[amk]匹配a、m或k
[^...]用来表示一组字符，比如[^abc]匹配除了a、b、c之外的字符
*     匹配0个或多个表达式
+     匹配1个或多个表达式
?     匹配0个或1个前面的正则表达式定义的片段，非贪婪模式
{n}   精确匹配n个前面的表达式
{n,m} 匹配n到m次由前面正则表达式定义的片段，贪婪模式
a|b   匹配a或b
()    匹配括号内的表达式，也表示一个组

# 模式修饰符
re.I 使匹配对大小写不敏感
re.L 做本地化识别(locale-aware)匹配
re.M 多行匹配 影响^和$
re.S 使.匹配包括换行在内的所有字符
re.U 根据Unicode字符集解析字符 这个标志影响\w \W \b \B
re.X 该标志通过给予你更灵活的格式以便你将正则表达式写的更易于理解
'''

