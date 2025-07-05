import random

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='')
        print()
def bin_search_rec(data,val,low,high):
    mid = (low+high)//2
    if val == data[mid]:
        return mid
    else:
        if low > high:
            return -1
        elif val < data[mid]:
            high = mid -1
        else:
            low = mid + 1
    return  bin_search_rec(data,val,low,high)

val=0
data=[]
while(len(data)<50):
    randNum = random.randint(1,100)
    if(randNum not in data):
        data.append(randNum)
data.sort()
showData(data)
val = int(input("請輸入1~100的數值"))
low = 0
high = len(data) - 1
inx = bin_search_rec(data,val,low,high)
if inx == -1:
    print("沒找到")
else:
    print(f"找到了編號是{inx}")
    
