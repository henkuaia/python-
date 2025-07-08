"""
数据容器之字符串操作
"""
name="zhangzuji"
# 通过下标所以取值
print(name[2])

# index 方法
print(name.index('zu'))
# replace 方法
name1=name.replace('z','a') # 将字符串name中全部的'z'替换为'a'
                                       # 注意不是修改字符串本身，而是得到了一个新的字符串
print(name1)

name="zhangzuji"
name2=name.replace('zhang','liu')# 将字符串name中全部的'zhang'替换为'liu'
print(name2)

# split 方法---字符串的分割
name="zhang zu ji"
my_list=name.split('z')
print(my_list)
my_list1=name.split(' ')
print(my_list1)

# strip 方法
name=" zhang zu ji "
name3=name.strip()
print(name3)
name="zhang zu jizh"
name4=name.strip("zh")
print(name4)
# 统计字符串中某字符出现次数

# 统计字符串长度





