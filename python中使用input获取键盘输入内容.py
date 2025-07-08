"""
python中使用input获取键盘输入内容
"""
name = input("请告诉我你是谁\n")
print("我知道了你是：%s"%(name))
# 输入数字类型
num = int(input("你的qq号是:\n"))# input输入的默认是字符串类型的，需要用int进行数据转换
print("我知道了，你的qq号是：%d"%(num))