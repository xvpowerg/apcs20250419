h = int(input("輸入樹高"))
d = int(input("白天上升公尺數"))
n = int(input("晚上下降公尺數"))
height = d
days = 1
while height < h:
    height -= n
    height += d
    days += 1

print(f"{days}爬上屋頂")
