import random

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='')
        print()

val=0
data=[]
while(len(data)<50):
    randNum = random.randint(1,100)
    if(randNum not in data):
        data.append(randNum)
showData(data)
val = int(input("請輸入1~100的數值"))
n = len(data)
for i in range(n):
    if data[i] == val:
        print(f"存在編號{i+1} 數值:{val}")
        break
else:
    print(f"不存在")

#存在顯示編號 數值
#存在顯示不存在
