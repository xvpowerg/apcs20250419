#5~20
#完成一個函式printLoop() 可顯示5~20
#完成以下功能呼叫函式printLoop(6,25) 會顯示6 7 8 9 ~25 printLoop(2,7) 2 3 4 ~ 7
def printLoop(s,e):
    for i in range(s,e+1):
        print(i,end=" ")
    print()

printLoop(6,25)
printLoop(2,7)
