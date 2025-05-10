height =  float(input("請輸入身高 單位公分:"))
weight = int(input("請輸入體重 單位公斤:"))
bmi = weight / ((height/100) ** 2)
print(f"bmi:{bmi:.2f}")
if bmi < 18.5:
    print("飄了")
elif bmi >= 18.5 and bmi <= 25:
    print("正常")
elif bmi > 25 and bmi <= 30:
    print("過重")
else:
    print("胖胖")
