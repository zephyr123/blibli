#-*- coding:utf8 -*-
class A:
    pass
class B(A):
    pass
class C:
    pass

print(issubclass(B,A))
print(issubclass(B,B))
print(issubclass(B,object)) #object是所有类的基类
print(issubclass(A,B))