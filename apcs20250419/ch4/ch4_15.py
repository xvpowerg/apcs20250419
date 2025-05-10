a = 5
def func():
    global a
    a += 1
    print("func:",a)
print("out 1:",a)
func()
print("out 2:",a)
