import sys

while True:
    tmp = input("请输入需要查询到分数:")
    num = int(tmp)
    if num == 100:
        print("S")
    elif 100 > num >= 90:
        print("A")
    elif 90 > num >= 80:
        print("B")
    elif 80 > num >= 60:
        print("C")
    elif num < 60:
        print("D")
    else:
        print("分数不合法！，程序退出！")
        sys.exit()