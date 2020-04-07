#-*- coding:utf8 -*-
class A:
    pass
class B(A):
    pass
class C:
    pass
b1 = B()
print(isinstance(b1,B))
print(isinstance(b1,A))
print(isinstance(b1,C))
print(isinstance(b1,(A,B,C)))