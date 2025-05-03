## 請寫一個程式，顯示由1至1000之間的費伯那西數列
"""
0 1 2 3 4 5 6 7   8  9
0 1 1 2 3 5 8 13  21 34
"""
max = int(input("費事系數範圍"))
num1,num2 = 1,1
print(num1,num2,sep=",",end="")
next = num1 + num2
while next <= max:
        print(f",{next}",end="")
        num1 = num2
        num2 = next
        next = num1 + num2
    
