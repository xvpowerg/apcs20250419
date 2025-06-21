class Node():
    def __init__(self,data="None"):
        self.data = data
        self.next = None
    def __str__(self):
        return f"{self.data}"
class Linked_list():
    def __init__(self):
        self.head = None
    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def add(self,item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            return
        ptr = self.head
        while ptr.next:
              ptr = ptr.next
        ptr.next = newNode
    def getNode(self,index):
        ptr = self.head
        for i in range(index):
            ptr = ptr.next
            if ptr == None:
                break
        return ptr
linke = Linked_list()
linke.add(5)
linke.add(15)
linke.add(25)
linke.add(72)
linke.print_list()
print("index:")
print(linke.getNode(2))
