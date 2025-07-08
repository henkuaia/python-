"""
if-elif-else判断语句的使用
"""
num=int(input("欢迎来到蓝天动物园\n 请输入您的身高:"))
vip=int(input("请输入您的vip等级\n"))
if num<=120 :
    print("您的身高未超过120，可以免费游玩\n祝你游玩愉快")
elif vip>=3 :
    print("您的vip等级超过3，可以免费游玩\n祝你游玩愉快")
else :
    print("您的身高超过120，且vip等级小于3，游玩需支付票价50元\n祝你游玩愉快")
