def testAge(age):
    if age >=0 and age<= 200:
        print("正確")
    else:
        raise Exception(f"錯誤的年齡:{age}")

testAge(10)
testAge(-20)
