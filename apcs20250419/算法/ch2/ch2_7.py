x = [5, 15, 25, 35, 45]                 # 建立無號整數陣列
for data in x:
    print(data,end=" ")
print()
x.insert(2,100)
print(x)
x.append(100)
print(x)
x[2] = 20
print(x)
x.remove(20)
print(x)
n = x.pop(2)
print(n)
print(x)
