a1 = int(input("首相"))
r = int(input("公比"))
n = int(input("項數"))

for i in range(n):
    print(a1 * r ** i,end=" ")
print()

def getAn(n):
    if n == 1:
        return a1
    else:
        return getAn(n-1) * r
    
print(getAn(n))
