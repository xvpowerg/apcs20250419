class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __lt__(self,other):
        self_msg = (self.x ** 2) + (self.y ** 2)
        other_msg = (other.x ** 2) + (other.y ** 2)
        return self_msg < other_msg

p1 = Point(2,9)
p2 = Point(3,18)
p3 = Point(1,2)
p4 = Point(7,3)

pList = [p1,p2,p3,p4]

pList.sort()
for p in pList:
    print(p)
