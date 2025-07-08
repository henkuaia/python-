"""
演示对list列表循环(遍历)
"""
flag = 0
my_list = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']

def func_while_list():
    global flag
    while flag < len(my_list):
        message = my_list[flag]
        print(message)
        flag = flag + 1


def func_for_list():
    for i in my_list:
        print(i)

func_while_list()
print()
print()
print()
func_for_list()