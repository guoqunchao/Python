import random
import sys
secret = random.randint(1,10)
while True:
    temp = input("不妨猜一下小甲鱼现在心情想的是哪个数字: ")
    if temp.isdigit():
        guess = int(temp)
    else:
        print("\"",temp,"\"","输入非法!")
        sys.exit(1)
    guess = int(temp)
    if guess == secret:
        print("哇 你太厉害了！")
        break
    elif guess > secret:
        print("哥哥 大了大了！")
    else:
        print("弟弟 小了小了")
print("拜拜~  游戏结束！")