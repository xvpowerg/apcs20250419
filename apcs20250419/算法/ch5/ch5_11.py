import random

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='')
        print()

def bin_search(data,val):
    low,high = 0,len(data)-1
    mid = -1
    while low <= high:
        mid = (low+high) // 2
        if val < data[mid]:
            high = mid - 1
        elif val > data[mid]:
            low = mid + 1
        else:
            return mid
    return -1

val=0
data=[]
while(len(data)<50):
    randNum = random.randint(1,100)
    if(randNum not in data):
        data.append(randNum)
data.sort()
showData(data)
val = int(input("請輸入1~100的數值"))
inx = bin_search(data,val)
if inx == -1:
    print("找不到")
else:
    print(f"找到了 位置在{inx + 1}")
