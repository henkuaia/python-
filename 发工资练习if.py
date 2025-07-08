"""
发工资练习
"""
import random

num = 0
k = 10000
for i in range(1, 21):
    j = random.randint(1,10)
    if j < 5:
        print(f"员工{i},绩效分{j}，低于5，不发工资")
    else:
    if k > 0:
        k = k - 1000
    print(f"员工{i}，发放工资1000，账户余额{k}")

print("工资发完了，下个月领取吧")
