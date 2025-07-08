"""
随机数
"""
import random
num = random.randint(1, 10)
a=int(input("请输入第一次猜的数字\n"))
flag=0
if a>num :
    print("大了")
elif a<num:
    print("小了")
else:
    print("你第一次就猜对了")
    flag=1
if flag==0:
    b = int(input("请输入第二次猜的数字\n"))
    if b > num:
        print("大了")
    elif b < num:
        print("小了")
    else:
        print("你第二次就猜对了")
        flag = 1
if flag == 0:
    c=int(input("请输入第三次猜的数字\n"))
    if c > num:
        print("你没有猜中")
    elif c < num:
        print("你没有猜中")
    else:
        print("你第三次就猜对了")
        flag = 1