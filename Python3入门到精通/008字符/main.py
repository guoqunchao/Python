# 取字符
str1 = "bailixuance"
print(str1[:5])

# 拼接字符
str2 = str1[:5] + " shouyue " + str1[5:]
print(str2)

# 首字符改大写
str3 = "xiaoxie"
print(str3.capitalize())

# 所有字符改小写
str4 = "XiaoBai"
print(str4.casefold())

# 字符串居中 空格填充
str5 = "juzhong"
print(str5.center(10))

# 统计次数
str6 = "tongjicishu"
print(str6.count("i"))

#  检查结束字符
str7 = "libai"
print(str7.endswith("ai"))


# 查找索引 无则-1
str8 = "wangzhexiagu"
print(str8.find("gu"))

# 查找索引 无则异常
str9 = "wangzhexiagu"
print(str9.index("gu"))


# 字符串作为分割
str10 = "wangzherongyao"
print(str10.join('++'))

# 删除空格或指定字符
str11 = "  ssssaaasssaaaass      "
str11 = str11.strip()
str11 = str11.strip('s')
print(str11)
