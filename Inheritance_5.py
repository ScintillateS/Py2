class A:
    def __init__(self):
        self._x = 5

class B(A):
    def display(self):
        print(self._x)

def main():
    obj = B()
    obj.display()
main()