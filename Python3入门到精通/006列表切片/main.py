member = ['小布丁','黑夜','迷途']

# 追加列表
member.append('超超')
print(member)

# 批量追加列表
member.extend(['a','b'])
print(member)

# 插入列表
member.insert(1,'赛维')
print(member)

# 交换元素
tmp = member[0]
member[0] = member[1]
member[1] = tmp
print(member)

# 删除元素
member.remove('a')
print(member)

# 删除最后一个元素
member.pop(1) # member.pop() 
print(member)

del member[0] # del member
print(member)

# +
list1 = [0,1,2,3]
list2 = [4,5,6,7]
list3 = list1 + list2
print(list3)

# *
list3 *= 3
print(list3)

# in 
list1 = [123,['小甲鱼','牡丹'],456]
print('小甲鱼' in list1[1])

# not in
print('超超' not in list1)

# clear
list4 =[1,2,3,4]
list4.clear()
print()

# count
list5 = [1,2,3,1,1,4]
print(list5.count(1))

# sort
list6 = [1,2,3,1,1,4]
list6.sort()
print(list6)

# reverse
list6.reverse()
print(list6)

# sort reverse
list7 = [1,435,64,12,1890]
list7.sort(reverse=True)
print(list7)

# index
list8 = [1,435,64,12,1890]
print(list8.index(435))