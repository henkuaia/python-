"""
ATM有函数版本
"""
money = 5000000
name: str = input("Enter your name: \n")
flag = 0


def yu_e(data):
    if data:
        print("------查询余额------")
    print(f"尊敬的{name}您好，您的的余额为{money}")
    return None


def cun_kuan():
    global money
    print("-------存款-------")
    k = int(input("请输入您的存款金额"))
    money = money + k
    yu_e(False)
    return None


def qu_kuan():
    global money
    print("-------取款-------")
    j = int(input("请输入您的取款金额"))
    if j > money:
        print("取款金额大于余额，取款失败")
    else:
        money = money - j
    yu_e(False)
    return None


def main():
    print("输入数字进行操作\n")
    print("1.查询余额\t")
    print("2.存款\t")
    print("3.取款\t")
    print("4.退出\t")


while flag == 0:
    main()
    num = int(input())
    if num == 1:
        yu_e(True)
    elif num == 2:
        cun_kuan()
    elif num == 3:
        qu_kuan()
    elif num == 4:
        print("程序退出，欢迎下次光临")
        flag = 1
    else:
        print("输入错误，程序退出")
        flag = 1
