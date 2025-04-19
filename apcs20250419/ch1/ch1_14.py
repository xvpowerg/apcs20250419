height = float(input("請輸入身高 單位公分:"))
weight = int(input("請輸入體重 單位公斤:"))
bmi = weight / ((height / 100) ** 2)
newBmi = round(bmi,2)
print("bmi:",bmi)
print("newBmi:",newBmi)
print("bmi:%.2f"%(bmi))

