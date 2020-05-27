import sys

while True:
    tmp = input("请输入需要查询到分数:")
    num = int(tmp)
    if tmp == '100':
        print("S")
    elif num >= 90 and num < 100:
        print("A")
    elif num < 90 and num >= 80:
        print("B")
    elif num < 80 and num >= 60:
        print("C")
    elif num < 60:
        print("D")
    else:
        print("分数不合法！，程序退出！")
        sys.exit()