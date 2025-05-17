class Employee:
    def __init__(self,name,salary=20000):
        self.name = name
        self.salary = salary
    def printInfo(self,title):
        print("title:",title)
        print("Name:",self.name)
        print("Salary:",self.salary)
emp1 = Employee("Iris",32000)
emp2 = Employee("Joy",43000)
#print(emp1.name,emp1.salary)
#print(emp2.name,emp2.salary)
emp1.printInfo("員工資訊1:")
emp2.printInfo("員工資訊2:")
