class Shape:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    def display(self):
        print(f"The shape is a {self.name}, and there are {self.sides} sides.")

class Rectangle(Shape):
    def __init__(self, name, sides, length, width):
        super(). __init__(name, sides)
        self.length = length
        self.width = width

    def display(self):
        super().display()
        area = self.length * self.width
        print(f"Your length is {self.length}.")
        print(f"Your width is {self.width}.")
        print(f"Your area is {area}.")

class Circle(Shape):
    def __init__(self, name, sides, radius):
        super(). __init__ (name, sides)
        self.radius = radius

    def display(self):
        super().display()
        area = self.radius * self.radius * 3.14
        circumference = self.radius * 2 * 3.14
        print(f"Your radius is {self.radius}.")
        print(f"Your area is {area}.")
        print(f"Your circumference is {circumference}")

d = Rectangle("Rectangle", 4, 56, 100)
d2 = Circle("Circle", 0, 10)
d2.display()