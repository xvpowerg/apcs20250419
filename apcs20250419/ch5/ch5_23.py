class MyForLoopBreakEx(Exception):
    pass
try:
    for i in range(1,3):
        print("i:",i)
        for k in range(1,4):
            print("k:",k)
            for j in range(1,3):
                 if i==2:
                    raise MyForLoopBreakEx
                 print("j:",j)
            print("==================")    
except:
    pass


            
