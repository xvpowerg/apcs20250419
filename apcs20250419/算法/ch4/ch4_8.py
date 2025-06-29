def josephus(ls,skip):
    idx = skip - 1
    while len(ls) > 1:
        print(ls,end=" ")
        print(ls.pop(idx))
        idx = (idx + skip - 1) % len(ls)
    print("ans:",ls[0])

n = int(input("輸入總人數"))
m = int(input("淘汰距離"))
list1 =[i for i in range(1,n+1)]
josephus(list1,m)
