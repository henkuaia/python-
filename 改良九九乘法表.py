for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i:<3}", end=' ')  # <3 表示左对齐，占3个字符
    print()