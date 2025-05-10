myData = []
for i in range(1,4):
    v = input(f"請輸入第{i}筆資料:")
    myData.append(v)
myData =list(map(int,myData)) 
print(myData)
total = 0
for d in myData:
    total += d
print(total)
