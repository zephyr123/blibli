# coding:utf8
class Nstr(str):
    def __lshift__(self, other):
        return self[other:] + self[:other]
    def __rshift__(self, other):
        return self[-other:] + self[:-other]

a = Nstr('I love Fish.com')
print(a << 3)
print(a >> 4)