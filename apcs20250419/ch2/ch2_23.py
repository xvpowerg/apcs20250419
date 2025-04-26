#輸入年齡
#>=18成年
#未成年
age = int(input("請輸入年齡"))
"""
if age >= 18:
    print("成年")
else:
    print("未成年")
"""    
msg = "成年" if age >= 18  else "未成年"

print(msg)
