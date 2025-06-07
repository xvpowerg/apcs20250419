def dec_to_bin(num):
    myList = []
    while True:
        num,reminder = divmod(num,2)
        myList.append(str(reminder))
        if num == 0:
            return "".join(myList[::-1])
def dec_to_oct(num):
    myList = []
    while True:
        num,reminder = divmod(num,8)
        myList.append(str(reminder))
        if num == 0:
            return "".join(myList[::-1])
def dec_to_hex(num):
    base = ("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F")
    myList = []
    while True:
        num,rem = divmod(num,16)
        myList.append(base[rem])
        if num == 0:
            return "".join(myList[::-1])
testNum = int(input("輸入10進位整數"))
print("二進位:",dec_to_bin(testNum))
print("8進位:",dec_to_oct(testNum))
print("16進位:",dec_to_hex(testNum))
