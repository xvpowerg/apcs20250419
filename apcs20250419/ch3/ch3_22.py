result = {"David":0,"Amy":0,"Sean":0}
for i in range(5):
    vote = input("投票給:")
    if vote not in result:
        print("選票無效")
        continue
    result[vote] +=  1

print("選舉結果:")
print(result)
