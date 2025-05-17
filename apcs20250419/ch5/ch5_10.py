scores={'Ch':100,'En':80, 'Ma':95}
print(scores["Ch"])
print(scores.get("Ch"))
print(scores.get("AA","Empty"))

print(scores.pop("En"))
print(scores)
print(scores.pop("BB","N/A"))
