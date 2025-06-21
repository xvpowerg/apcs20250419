class Stack():
    def __init__(self):
        self.my_stack = []
    def my_push(self,data):    
        self.my_stack.append(data)
    def my_pop(self):
        return self.my_stack.pop()
    def size(self):
        return len(self.my_stack)

stack = Stack()

fruits = ['Apple', 'Banana', 'Cherry', 'Mango']
for f in fruits:
    stack.my_push(f)
    
print(stack.size())

print(stack.my_pop())
