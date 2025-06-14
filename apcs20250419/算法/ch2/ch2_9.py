myList = []
#1~100
for i in range(1,101):
    myList.append(i)
print(myList)
myList2 = [x for x in range(1,101)]
print(myList2)

y = [x**2 for x in range(1,11)]
print(y)
z = [x for x in range(11) if x % 2 != 0]
print(z)
