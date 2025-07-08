"""
ATM有函数版本
"""
money = 5000000
name = input("Enter your name: \n")
flag = 0
def yue():
    print(f"尊敬的{name}您好，您的的余额为{money}")
    return None
def cunkuan():
    global money
    k = int(input("请输入您的取款金额"))
    money = money + k
    print(f"尊敬的{name}您好，您的的余额为{money}")
    return None
def qukuan():
    k = int(input("请输入您的取款金额"))
    money = money - k
    print(f"尊敬的{name}您好，您的的余额为{money}")
    return None
while (flag == 0):

    print("输入数字进行操作\n1.查询余额\t2.存款\t3.取款\t4.退出\t")
    num = int(input())
    if num == 1:
        print(f"尊敬的{name}您好，您的的余额为{money}")
    elif num == 2:
        k = int(input("请输入您的取款金额"))
        money = money + k
        print(f"尊敬的{name}您好，您的的余额为{money}")
    elif num == 3:
        k = int(input("请输入您的取款金额"))
        money = money - k
        print(f"尊敬的{name}您好，您的的余额为{money}")
    elif num == 4:
        print("程序退出，欢迎下次光临")
        flag = 1
    else:
        print("输入错误，程序退出")
        flag = 1
