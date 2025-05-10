str1 = ","
nameList = ["Ken","Vivin","Iris"]
msg = ""
for i in range(len(nameList)):
    if i != 0:
        msg+=str1
    msg+=nameList[i]
    """
    if i < len(nameList) - 1:
        msg+=str1
    """

print(msg)#Ken,Vivin,Iris

