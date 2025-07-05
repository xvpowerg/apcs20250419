def combine(lst,n):
    if len(lst) == n:
        return [lst]
    elif n == 1:
        return [[x] for x in lst]
    else:
        out = []
        for i in range(len(lst) - n +1):
            for c in  combine(lst[i+1:],n-1):
                out.append([lst[i]] + c)
        return out
    
myList = combine([1,2,3,4,5,6],4)
for v in myList:
    print(v)
                
