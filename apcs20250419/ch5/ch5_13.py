class Employee:
    def __init__(self,name,salary=20000):
        self.name = name
        self.salary = salary
emp1 = Employee("Sean",50000)
print(emp1.name,emp1.salary)
emp2 = Employee("Ken",62000)
print(emp2.name,emp2.salary)
emp3 = Employee("Iris")
print(emp3.name,emp3.salary)
