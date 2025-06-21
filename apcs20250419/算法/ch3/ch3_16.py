for i in range(1,7):
    for j in range(1,7):
        if j <= i:
            continue
        for k in range(1,7):
            if k <= j:
                continue
            for l in range(1,7):
                if l <= k:
                    continue
                print(f"{i}{j}{k}{l}")    
