class Person:
    count = 0
    def __init__(self,name,age=0):
        Person.count += 1
        self.name = name
        self.age = age
    def printInfo(self):
        print("name:",self.name)
        print("age:",self.age)
    def printTotal():
        print(Person.count)
p1 = Person("Ken",21)
p2 = Person("Iris",23)
p3 = Person("Vivin",31)
p4 = Person("Lucy",31)
p1.printInfo()
p2.printInfo()
p3.printInfo()

Person.printTotal()
    
