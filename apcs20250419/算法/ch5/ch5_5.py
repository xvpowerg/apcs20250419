def sqrt_binary(x,pre=2):
    min,max = 0,x
    while (max - min) > 10 ** -pre:
        mid = (max+min) / 2
        if mid*mid > x:
            max = mid
        else:
            min = mid
    return mid

num = int(input("輸入整數"))
print(f"{num}的平方根{sqrt_binary(num):.2f}")
