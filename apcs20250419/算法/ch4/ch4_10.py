def factor_for(n):
    result = 1
    for i in range(n,0,-1):
        result*=i
    return result

def factor_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factor_recursive(n -1)

n = int(input("請輸入階乘數"))
print(f"{n}!:{factor_for(n)}")
print(f"{n}!:{factor_recursive(n)}")
