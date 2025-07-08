"""
演示数据容器--集合的使用
"""

# 定义集合
my_set = {"张无忌", "张三丰", "德玛西亚", "黑马程序员", "张无忌", "张三丰", "德玛西亚"}
set1 = set()
print(f"my_set的内容是{my_set}my_set的类型是{type(my_set)}")
print(f"set1的内容是{set1}set1的类型是{type(set1)}")
# 添加新元素
my_set.add("亚索")
print(f"my_set的内容是{my_set}")
my_set.add("张无忌")
print(f"my_set的内容是{my_set}")
# 移除元素
my_set.remove("亚索")
print(f"my_set的内容是{my_set}")
# 随机取出一个元素
ele=my_set.pop()
print("ele=",ele)
print("my_set=",my_set)
# 清空集合
my_set.clear()
print("my_set=",my_set)
# 取2个集合的差集
set2={1,2,3,4,5}
set3={5,6,7,8,9}
set4=set2.difference(set3)
print(set2)
print(set3)
print(set4)
# 消除2个集合的差集
set2.difference_update(set3)
print(set2)
print(set3)
# 2个集合合并为1个
set5=set2.union(set3)
print(set5)
# 统计集合元素数量
print("len(set5)=",len(set5))
# 集合不支持下标索引，不能用while循环
# 可以用for循环
for i in set5:
    print(i)