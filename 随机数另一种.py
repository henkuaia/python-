"""
随机数
"""
import random
num = random.randint(1, 10)
a=int(input("请输入第1次猜的数字\n"))
flag=0
if a==num:
    print("恭喜你第1次猜对了")
else:
    if a>num:
        print("大了")
    else :
        print("小了")
    a = int(input("请输入第2次猜的数字\n"))
    if a==num:
        print("恭喜你第2次猜对了")
    else:
        if a>num:
            print("大了")
        else:
            print("小了")
        a = int(input("请输入第3次猜的数字\n"))
        if a==num:
            print("终于猜中了")
        else:
            print("sorry，您最终没有猜中")
