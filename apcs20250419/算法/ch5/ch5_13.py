btree = ["-"]*2**3
btree[1]  = "A"
btree[2] = "B"
btree[3] = "C"
btree[5] = "D"
btree[7] = "E"

print(f"{btree[2]}父節點:{btree[2//2]}")
print(f"{btree[3]}父節點:{btree[3//2]}")

print(f"{btree[1]}的左子節點{btree[2*1]}")
print(f"{btree[1]}的右子節點{btree[2*1 + 1]}")

for i in range(1,len(btree)):
    print(f"btree[{i}] = {btree[i]}",end=" ")
    if 2*i+1 <len(btree):
        print(f"({btree[2*i]},{btree[2*i + 1]})")
    else:
        print()
