p10x5 = [[''] * 5  for i in range(10)]

for i in range(10):
    for j in range(5):
        p10x5[i][j] = f"({i},{j})"

for i in range(10):
    for j in range(5):
        print(p10x5[i][j],end = " ")
    print()    
