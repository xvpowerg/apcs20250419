class Employee:
    company="GJ"
    phone = "(02)2311-4537"
    def __init__(self,name,salary=20000):
        self.name = name
        self.salary = salary
    def printInfo(self,title):
        print("title:",title)
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Company:",Employee.company)
        print("Phone:",Employee.phone)
emp1 = Employee("Sean",50000)
emp2 = Employee("David")
emp1.printInfo("員工資訊1")
emp2.printInfo("員工資訊2")
print("=========")
emp1.name = "Iris"
emp1.printInfo("員工資訊1")
emp2.printInfo("員工資訊2")
print("=========")
Employee.company = "IBM"
emp1.printInfo("員工資訊1")
emp2.printInfo("員工資訊2")


