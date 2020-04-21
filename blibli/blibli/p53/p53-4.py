#coding:utf8
class A:
    def __init__(self,x):
        x = x + 1
        self.v1 =x
class B(A):
    def __init__(self,x):
        x = x + 1
        self.v2 = x
b = B(8)
print('%d%d' % b.v1,b.v2)