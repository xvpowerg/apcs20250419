def is_prime(num):
    for i in range(2,int(num**0.5) + 1):
            if num % i == 0:
                return False
    return True

def primeList(num):
    primes = []
    for n in range(2,num+1):
        if is_prime(n):
            primes.append(n)
    return primes

n = int(input("輸入一個正整數"))
pNumbers = primeList(n)
print(f"小於等於{n}的質數:",pNumbers)
