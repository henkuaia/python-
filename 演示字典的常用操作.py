"""
演示字典的常用操作
"""
my_dict = {"张无忌": 99, "张三丰": 77, "德玛西亚": 72, "周杰伦": 83, "盖伦": 62}
# 新增元素
# 更新元素
print(my_dict)
# 删除元素
my_dict.pop("盖伦")
print(my_dict)
# 清空元素
my_dict.clear()
print(my_dict)
# 获取全部的key
my_dict = {"张无忌": 99, "张三丰": 77, "德玛西亚": 72, "周杰伦": 83, "盖伦": 62}
print(my_dict.keys())
# 遍历字典
# 方式1 通过获取到全部的key来完成遍历
for key in my_dict.keys():
    print(f"字典的key是{key}  ",end='')
    print(f"key对应的value是{my_dict[key]}")
# 方式2 对字典进行for循环，每一次都是直接得到对应的key
for key in my_dict:
    print(f"字典的key是{key}  ",end='')
    print(f"key对应的value是{my_dict[key]}")

# 统计字典内的元素数量
print(len(my_dict))
