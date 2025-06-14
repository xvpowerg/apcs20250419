scores=[87,66,90,65,70]
score_sum = 0
counts = len(scores)
score_max = 0
score_min = 100
for i in range(counts):
    print(f"{scores[i]}")
    score_sum += scores[i]
    if scores[i] > score_max:
        score_max = scores[i]
    if  scores[i]  < score_min:
        score_min = scores[i]

print(f"max:{score_max}")
print(f"min:{score_min}")
print(f"sum:{score_sum}")


print(f"max:{max(scores)}")
print(f"min:{min(scores)}")
print(f"sum:{sum(scores)}")

