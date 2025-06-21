class Queue():
    def __init__(self):
        self.my_queue = []
    def enqueue(self,data):
        self.my_queue.append(data)
    def dequque(self):
        return self.my_queue.pop(0)
    def size(self):
        return len(self.my_queue)
    def isEmpty(self):
        return self.size() == 0
queue = Queue()
print("size:",queue.size())
print("isEmpty:",queue.isEmpty())
people = ['Amy', 'David', 'Sean']
for p in people:
    queue.enqueue(p)
print("size:",queue.size())
print("isEmpty:",queue.isEmpty())

while not queue.isEmpty():
    print(queue.dequque())

