from itertools import permutations
listto9 = [1,2,3,4,5,6,7,8,9]
plist = list(permutations(listto9))

def n1minusn2(myList):
    n1 = myList[0] * 10000 + myList[1] * 1000 + myList[2] * 100+ myList[3] * 10+ myList[4]   
    n2 = myList[5] * 1000 + myList[6] * 100+ myList[7] * 10+ myList[8]
    ans = n1 - n2
    return (n1,n2,ans)
for myList in plist:
    if myList[4] - myList[8] == 6 or myList[8] - myList[4] == 4:
        n1,n2,ans = n1minusn2(myList) 
        if ans == 66666:
            print(f"{n1}-{n2} = 66666")
        
