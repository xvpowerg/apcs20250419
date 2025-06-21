class Node():
    def __init__(self,data="None"):
        self.data = data
        self.next = None

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
linke = Linked_list()
linke.add(5)
linke.add(15)
linke.add(25)
linke.print_list()
