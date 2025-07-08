"""
字符串操作练习
"""
name="ithima itcast boxuegu"
# 统计字符串内有多少个"it"字符
num=name.count("it")
print(num)

# 将字符串内的空格，全部替换为字符："|"
name1=name.replace(" ","|")
print(name1)

# 按照"|"进行字符串分割，得到列表
list1=name1.split("|")
print(list1)
print(type(list1))



