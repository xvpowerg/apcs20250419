num = int(input("陣列長度"))
arr = [0] * num
for i in range(num):
    arr[i] = int(input(f"第{i+1}筆輸入整數:"))
for j in range(num-1):
    if arr[j] >= arr[j+1]:
        print("不是遞增")
        break
else:
    print("是遞增")     

for k in range(num-1):
    if arr[k] *arr[k+1] >=0:
        print("不是正負交錯")
        break
else:
    print("正負交錯")

    
