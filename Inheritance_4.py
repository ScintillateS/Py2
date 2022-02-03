class A:
    def __init__(self):
        self.__x = 1

class B(A):
    def display(self):
        print(self.__x)

def main():
    obj = B()
    obj.display()
main()