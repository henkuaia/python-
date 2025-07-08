age=int(input("请输入您的年龄：\n"))
if age>=18:
    if age<30:
        if int(input("请输入您的入职时间：\n"))>2:
            print("欢迎您，您的入职时间大于2，请领取礼品")
        elif int(input("请输入您的级别：\n"))>3:
            print("欢迎您，您的级别大于3，请领取礼品")
        else:
            print("sorry,不可领取礼品")
else:
    print("sorry,不可领取礼品")