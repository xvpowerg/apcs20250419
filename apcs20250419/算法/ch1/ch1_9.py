a1 = int(input("首相"))
d = int(input("公差"))
n = int(input("項數"))

def genAn(n):
    if n == 1:
        return a1
    else:
        return genAn(n-1) + d

print(genAn(n))
