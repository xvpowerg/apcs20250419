class Stack():
    def __init__(self,capacity):
        self.my_stack = [None] * capacity
        self.top = -1
        self.capacity = capacity
        
    def push(self,data):
        if self.isFull():
            print("滿了")
        else:
            self.top += 1
            self.my_stack[self.top] = data
            
    def pop(self):
        if self.isEmpty():
            print("空的")
            return None
        else:
            data = self.my_stack[self.top]
            self.my_stack[self.top] = None
            self.top -= 1
            return data
        
    def size(self):
         return self.top + 1
        
    def isEmpty(self):
         return self.size() == 0
        
    def isFull(self):
         if self.top >= self.capacity - 1:
             return True
         else:
             return False
stack = Stack(3)
fruits = ['Apple', 'Banana', 'Cherry', 'Mango']
for f in fruits:
    stack.push(f)
for v in range(4):
    print(stack.pop())
