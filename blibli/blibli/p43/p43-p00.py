# coding:utf8
class Nstr(str):
    def __sub__(self, other):
        return self.replace(other,'')

a = Nstr('I love Fish!iiiiii')
b = Nstr('i')
print(a-b)