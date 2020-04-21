#coding:utf8
class A:
    def __init__(self,a,b,c):
        self.x = a + b + c
a = A(1,2,3)
b = getattr(a,'x')
setattr(a,'x',b+1)
print(a.x)