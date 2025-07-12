coinType = (50,10,5,1)
def exchange(amt):
    global count
    result = {}
    for coin in coinType:
        num = amt // coin
        result[coin] = num
        count += num
        amt %= coin

    return result
count = 0
amout = int(input("輸入金額"))
ans = exchange(amout)
for coin in coinType:
    print(f"{coin}元硬幣{ans[coin]}")
print(f"共{count}個硬幣")
