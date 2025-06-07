def func1():
    print("Test1")
def func2():
    func1()
    print("Test2")

def fun3():
   print("Test3") 
   fun3()
# 何時結束
# 之間的過程 你要處理甚麼?
def func4(n):
    print("Star:",n)
    if n <=3:
        print(n)
        func4(n+1)
    print("End:",n)    
    
"""
func1()
func1()
func1()
"""
"""
func2()
"""
#fun3()
func4(1)
