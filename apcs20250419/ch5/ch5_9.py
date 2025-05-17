scores={'Ch':100,'En':80, 'Ma':95}
print(scores)
add_dic= {"So":90}#key不存在加入
scores.update(add_dic)
print(scores)
update_dic = {"En":75,"Ma":100}
scores.update(update_dic)#key存在更新
print(scores)

scores["HR"] = 81
print(scores)
scores["Ch"] = 72
print(scores)
