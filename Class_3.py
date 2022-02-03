class Student:
    def __init__(self, number, name, m1, m2, m3):
        self.number = number
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def display(self):
        print(f"Hi {self.name}, your roll number is {self.number}.")
    def sum_of_marks(self):
        totalm = self.m1 + self.m2 + self.m3
        print('Total Mark: ', totalm)

name = input("What is your name?  ")
number = int(input("What is your roll number?  "))
m1 = int(input("What is your English mark?  "))
m2 = int(input("What is your Science mark?  "))
m3 = int(input("What is your Fitness mark?  "))

p1 = Student(number, name, m1, m2, m3)
#p1.m1 = 100
#p1.m2 = 100
#p1.m3 = 100
p1.display()
p1.sum_of_marks()
