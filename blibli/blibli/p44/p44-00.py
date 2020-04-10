#coding:utf8
class Nint(int):
    def __radd__(self, other):
        print("__radd__被调用了!")
        return int.__add__(self,other)

a = Nint(5)
b = Nint(3)
print(a+b)
print(1+b)