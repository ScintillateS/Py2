class Person:
    def __init__(self):
        self. name = "isfnifinfianfus"
        self. age = 6325435

    def printdetail(self):
        print(f"Your name is {self.name}.")
        print(f"Your age is {self. age}.")

    def inputdetail(self):
        self. name = input("What is your name?  ")
        self. age = int(input("What is your age?   "))
class Student(Person):
    pass
x = Student()
x.inputdetail()
x.printdetail()
