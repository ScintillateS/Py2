class A:
    def test1(self):
        print(" test of A called ")

class B(A):
    def test(self):
        print(" test of B called ")

class C(A):
    def test(self):
        print(" test of C called ")

class D(B, C):
    def test2(self):
        print(" test of D called ")

obj = D()
obj.test()