#輸入身分證字號
#判斷男女
#A123456789
#1 男 2是女 其他錯誤
pid = input("輸入身分證字號")

myId = int(pid[1])
if myId == 1:
    print("男")
elif myId == 2:
    print("女")
else:
    print("錯誤")
