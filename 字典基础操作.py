"""
字典基础操作
"""

# 定义字典
my_dict = {"张无忌": 99, "张三丰": 66, "德玛西亚": 72, "周杰伦": 83}
# 定义空字典
my_dict1 = {}
my_dict2 = dict()
print(f"my_dict={my_dict}类型是{type(my_dict)}")
print(f"my_dict1={my_dict1}类型是{type(my_dict1)}")
print(f"my_dict2={my_dict2}类型是{type(my_dict2)}")
# 定义重复Key的字典
my_dict = {"张无忌": 99, "张三丰": 66, "德玛西亚": 72, "周杰伦": 83, "张无忌": 100}  # 字典不可重复，重复会被视为更新
print(f"my_dict={my_dict}")
# 从字典中基于Key获取Value
x="张无忌"
print(f"{x}的考试分数是{my_dict[x]}")
# 定义嵌套字典
dict1={"张无忌":
           {"语文":77,"数学":66,"英语":33},
       "张三丰":
           {"语文":88,"数学":86,"英语":55},
       "东方不败":
           {"语文":99,"数学":96,"英语":66}}
# 从嵌套字典中获取数据
print(f"dict1={dict1}")
a="张无忌"
b="语文"
print(f"{a}的{b}成绩为{dict1[a][b]}")