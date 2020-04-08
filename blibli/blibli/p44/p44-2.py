#coding:utf8
class Nint(int):
    def __rsub__(self, other):
        return int.__sub__(self,other)

a = Nint(5)
print(3-a)
