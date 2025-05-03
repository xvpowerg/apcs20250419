myList = ["Apple","Banana","Cherry"]
key = "Kiwi"
print(key in  myList)
#如果key在myList 顯示 Banana在myList
#如果key不在myList 顯示 Banana不在myList
if key in myList:
    print(f"{key}在myList")
else:
    print(f"{key}不在myList")
