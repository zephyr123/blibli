# coding:utf8
class Nstr:
    def __init__(self,string):
        string_total = 0
        if isinstance(string,str):
            for i in string:
                string_total += ord(i)
            self.string = string_total

    def __add__(self, other):
        return self.string + other.string
    def __sub__(self, other):
        return self.string - other.string
    def __mul__(self, other):
        return self.string * other.string
    def __truediv__(self, other):
        return self.string / other.string
    def __floordiv__(self, other):
        return self.string // other.string

a = Nstr('abc')
b = Nstr('bc')
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
