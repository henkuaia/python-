"""
演示对序列进行切片操作
"""
# 对list进行切片，从1开始，4结束，步长1
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = list1[1:4]
print("list2为   ", end='')
print(list2)

# 对tuple进行切片，从头开始，到最后结束，步长1
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple3 = tuple1[0:9]
print("tuple3为  ", end='')
print(tuple3)
tuple2 = tuple1[0:10]
print("tuple2为  ", end='')
print(tuple2)
# 对str进行切片，从头开始，到最后结束，步长2
str1 = "zhangwuji"
str2 = str1[::2]
print("str2为    ", end='')
print(str2)
# 对str进行切片，从头开始，到最后结束，步长-1
str3 = str1[::-1]
print("str3为    ", end='')
print(str3)
# 对列表进行切片，从3开始，到1结束，步长-1
list3 = list1[3:1:-1]
print("list3为   ", end='')
print(list3)
# 对元组进行切片，从头开始，到尾结束，步长-2
tuple4 = tuple1[::-2]
print("tuple4为  ", end='')
print(tuple4)
