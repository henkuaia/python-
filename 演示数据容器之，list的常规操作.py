"""
演示数据容器之，list的常规操作
"""
# 查找元素下标
my_list = ['a', 'b', 'c']
num = my_list.index('c')
print(num)

# 修改特定位置的元素值
my_list[0] = 'A'
print(my_list[0])

# 指定位置插入元素
my_list.insert(1, 'a')
print(my_list)

# 追加元素,语法一
my_list.append('d')
print(my_list)

# 追加元素，语法二
my_list.extend(['e', 'f', 'g'])
print(my_list)

# 元素删除，语法一
del my_list[0]
print(my_list)

# 元素删除，语法二
my_list=['A', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
ele = my_list.pop(0)
print(my_list)
print(f"取出的元素是{ele}")

# 删除一个特定的元素
my_list.remove('a')
print(my_list)

# 清空列表
my_list.clear()
print(my_list)

# 统计某元素在列表内的数量
one_list = ['a', 'b', 'c', 'd', 'a', 'a', 'c']
k='c'
num=one_list.count(k)
print(f"one_list中'{k}'元素有{num}个")

# 统计列表内，有多少元素
print(f"one_list列表中有{len(one_list)}个元素")


