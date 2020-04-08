#coding:utf8
class Nint(int):
    def __new__(cls, inting):
        if isinstance(inting,str):
            return ord(inting)
        else:
            return int(inting)

print(Nint('a'))
print(Nint(56))
