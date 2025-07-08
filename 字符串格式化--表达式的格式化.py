"""
字符串格式化--练习
"""
name = "天源科技"# 公司名
stock_prise = "56"# 股票价格
stock_code = "516648"# 股票代码
flag = "1.8"# 股票每日增长系数
grow_day = "7"# 增长天数
message1=f"公司名称为：{name}   当前股票价格为：{stock_prise}   股票代码为{stock_code}"
message2="股票每日增长系数为：%2.1f   经过%d天的增长，当前股价为%4.2f"%(flag,grow_day,stock_prise*flag^7)
