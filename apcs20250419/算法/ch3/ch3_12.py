count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for l in range(1,5):
                if i!=j and i != k and i != l and j != k and j != l and k != l:
                    count+=1
                    print(f"{count}:{i}{j}{k}{l}")
                    
