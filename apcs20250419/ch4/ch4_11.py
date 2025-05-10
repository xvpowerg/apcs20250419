def personInfo(name,age,**other):
    print("===Info====")
    print("name:",name)
    print("age:",age)
    if "company" in other:
        print("公司是:",other["company"])
    for key in other:
        print(key,":",other[key])
        
personInfo("Sean",40)
personInfo("David",35,phone="080118",company="Google")
