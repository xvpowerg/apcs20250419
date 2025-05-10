myData = [1,2,3,4,5]
myData2 = [1,2,3,4,5]

def func1(v1,v2):
    return v1 + v2
def func2(v1,v2):
    return v1*v2
def func3(v1,v2):
    return v1 - v2

def changeData(myList,v):
    for i in range(len(myData)):
        myData[i] +=  v
        
def changeData2(myList,v,func):
    for i in range(len(myData2)):
        myData2[i] = func(myData2[i],v)
        
changeData(myData,10)
print(myData)
changeData2(myData2,2,func)
print(myData2)

