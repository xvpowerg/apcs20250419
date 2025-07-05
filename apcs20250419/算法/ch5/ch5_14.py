class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return f"{self.data}"

nodeA = Node(14)
nodeB = Node(3)
nodeC = Node(16)
nodeD = Node(23)
nodeE = Node(7)
nodeF = Node(20)

root = nodeA
root.left = nodeB
root.right = nodeE

nodeB.left = nodeC
nodeB.right = nodeD

nodeE.right = nodeF

print(f"{root.data} 左{root.left} 右{root.right}")


