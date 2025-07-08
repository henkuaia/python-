"""
元组常见操作----1
"""
# 定义元组
t1=(1,'a',True)
# 定义空元组
t2=()
t3=tuple()
print(f"t1的数据类型是{type(t1)},t1的内容是{t1}\t")
print(f"t2的数据类型是{type(t2)},t2的内容是{t2}\t")
print(f"t3的数据类型是{type(t3)},t3的内容是{t3}\t")
t4=('a')#定义了一个字符串
print(f"t4的数据类型是{type(t4)},t4的内容是{t4}\t")
t5=('a',)#定义了一个只有一个元素的元祖
print(f"t5的数据类型是{type(t5)},t5的内容是{t5}\t")
# 元组的嵌套
t6=((1,2,3),(4,5,6))
print(f"t6的数据类型是{type(t6)},t6的内容是{t6}\t")
# 元组下标索引取出内容
# for i in t6:
#     print(i)
flag=0
while flag<len(t6):
    print(t6[flag])
    flag+=1

message=t6[0][0]
print(message)

