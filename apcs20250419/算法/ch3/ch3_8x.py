class Stack():
    def __init__(self):
        self.mystack = []
    def my_push(self,data):
        self.mystack.append(data)
    def my_pop(self):
        return self.mystack.pop()
    def size(self):
        return len(self.mystack)
Fruits = ["apple","banana","cherry","mango"]
stack = Stack()
for i in Fruits:
    stack.my_push(i)
print(stack.size())
print(stack.my_pop())
