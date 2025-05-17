num1 = 10
num2 = 0
num3 = [1,3,5,7,9]
ans = 0
try:
    ans = num1 // num2
    #ans = num3[10]
except ZeroDivisionError:
    print("分母不可為0")
except IndexError:
    print("索引錯誤")

print(ans)
