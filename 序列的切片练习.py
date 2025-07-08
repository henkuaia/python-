"""
序列的切片练习
"""
my_str = "万过薪月，员序程马黑来，nohtyP学"
str1 = my_str[::-1]
print(str1)
str2 = str1[9:14]
print(str2)
list1 = my_str.split("，")
str3 = ""
str3 = list1[1].replace("来", "")
str4 = str3[::-1]
print(str3)
print(str4)
