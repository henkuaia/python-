"""
九九乘法表
"""
i=1
j=1
k=1
while i<10:
    j=1
    while j<=i:
        k=i*j
        print(f"{j}*{i}={k}  ",end='')
        j=j+1
    i=i+1
    print("\n")
