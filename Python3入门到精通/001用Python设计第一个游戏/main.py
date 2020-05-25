print("-------------------------------------")
a = 0
while a < 3:
    temp = input("不妨猜一下小甲鱼现在心情想的是哪个数字: ")
    guess = int(temp)
    a += 1
    if guess == 8:
        print("卧槽，你是小甲鱼心里的蛔虫吗？")
        print("哼，猜中了也没有奖励！")
        break
    else:
        if guess > 8:
            print("哥，大了大了")
        else:
            print("嘿，小了小了")
print("游戏结束，不玩啦O(∩_∩)O！")