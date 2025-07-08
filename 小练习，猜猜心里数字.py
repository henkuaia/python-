"""
小练习，猜猜心里数字
"""
num=10
if int(input("请输入第一次猜想的数字：\n"))==num:
    print("恭喜你第一次就猜对了")
elif int(input("不对，请再猜一次：\n"))==num:
    print("恭喜你猜对了")
elif int(input("不对，请猜最后一次：\n"))==num:
    print("恭喜你最终猜对了")
else :
    print("sorry 全部猜错了，我猜的是%d"%num)