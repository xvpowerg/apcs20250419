class Queue():
    def __init__(self,capacity):
            self.queue = []
            self.capacity = capacity
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        return self.size() == 0
    def isFull(self):
        return self.size() >= self.capacity
    def dequeue(self):
        if self.isEmpty():
            print("空")
            return None
        return self.queue.pop(0)
    def enqueue(self,data):
        if self.isFull():
            print("滿")
            return
        self.queue.append(data)
people = ['Amy', 'David', 'Sean', 'Nicole']
queue = Queue(3)
for p in people:
    queue.enqueue(p)
    
for i in range(4):
    print(queue.dequeue())
