for i in range(1,5):
    for j in range(1,5):
        if i == j:
            continue
        for k in range(1,5):
            if k == i or k == j:
                continue
            for l in range(1,5):
                    if l == i or l == j or l == k:
                        continue
                    print(f"{i}{j}{k}{l}")
