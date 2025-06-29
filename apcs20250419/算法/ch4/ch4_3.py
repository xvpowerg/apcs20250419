while True:
    n = int(input("輸入一個整數"))
    if n == -1:
        break
    print(f"{n}=",end=" ")
    while True:
        for i in range(2,int(n**0.5) + 1):
            if n % i == 0:
                n = int(n / i)
                print(f"{i}*",end="")
                break
        else:
            print(n)
            break
