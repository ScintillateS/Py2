class A:
    pass

class B(A):
    pass

obj = B()
print(isinstance(obj,B))