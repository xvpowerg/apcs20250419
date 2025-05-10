# 攝氏溫度轉換華氏溫度程式
def c2f(c):
    f = 9 / 5 * c +32
    return f

while True:
    inStr = input("輸入攝氏溫度(輸入q離開)")
    if inStr == 'q':
        break
    tc = float(inStr)
    tf = c2f(tc)
    print(f"華氏溫度:{tf:.2f}")
