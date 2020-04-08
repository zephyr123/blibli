# coding:utf8
class Nstr(str):
    def __lshift__(self, other):
        return str(self) << str(other)
    def __rshift__(self, other):
        return str(self) >> str(other)

a = Nstr('I love FishC.com')
print(a << 3)
