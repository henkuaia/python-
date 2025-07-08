"""
遍历练习
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
one_list = []
flag = 0
# while flag < len(my_list):
#     if my_list[flag] % 2 == 0:
#         #one_list.extend([my_list[flag]])#第一种方法
#         one_list.append(my_list[flag])#第二种方法
#     flag += 1
for i in my_list:
    if i%2 == 0:
        # one_list.extend([i])#第一种方法
        one_list.append(i)#第二种方法
    flag += 1

print(one_list)
