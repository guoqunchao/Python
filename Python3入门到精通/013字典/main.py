# -*- conding:utf-8 -*-

dict01 = {}
print(dict01.fromkeys((1,2,3)))
print(dict01.fromkeys((1,2,3), 'Numbers'))
print(dict01.fromkeys((1,2,3),('one','two','three')))

dict01 = dict01.fromkeys(range(1,33),'赞')
print(dict01)
for eachKey in dict01.keys():
    print(eachKey)

for eachValue in dict01.values():
    print(eachValue)

for eachItem in dict01.items():
    print(eachItem)

# 判断key是否存在
print(dict01.get(32))
print(31 in dict01)
print(33 in dict01)
 
# 清除字典
dict01.clear()
print(dict01)