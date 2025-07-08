"""
函数嵌套
"""
def function_b():
    print("---2---")
    return None
def function_a():
    print("---1---")
    function_b()
    print("---3---")
    return None
function_a()





