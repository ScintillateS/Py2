class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Your name is {self.name}.")
        print(f"Your salary is {self.salary}.")

class Employee(Person):
    def __init__(self, name, salary, ID):
        Person. __init__(self, name, salary)
        self.ID = ID

    def display2(self):
        Person.display(self)
        print(f"Your ID is {self.ID}.")
p = Employee("James", 10000, 123123)
#p.display()
p.display2()