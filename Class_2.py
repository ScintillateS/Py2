class Person:
    def __init__(self, name, age):
        self.name = name
        self. age = age
    def display(self):
        print("The name is ",self.name, " and the age is ", self.age, ".")

p1 = Person("John", 36)
p1.display()

p2 = Person("James", 50)
p2.display()
