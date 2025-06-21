##質數驗證練習
def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True    

n = int(input("輸入一個整數"))

if is_prime(n):
    print(f"{n}是質數")
else:
    print(f"{n}不是質數")
