'''
def fun(x):
    result = x
    for i in range(1,x):
        result = result * i
    return result
number = int(input("请输入一个正整数："))
result = fun(number)
print("\"%d\" 的阶乘是 \"%d\"" %(number,result))
'''

def Recursive(x):
    if x == 1:
        return 1 
    else:
        return x * Recursive(x - 1)
print(Recursive(5))