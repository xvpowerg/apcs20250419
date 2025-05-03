subjs = ["國文","數學","英文"]
scores = [100,80,95]

for i in range(len(subjs)):
    print(f"{subjs[i]}:{scores[i]}")
print()

print(list(zip(subjs,scores)))
for n,s in zip(subjs,scores):
    print(f"{n}:{s}")
"""
國文:100
數學:80
英文:95
"""
