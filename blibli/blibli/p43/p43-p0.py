# coding:utf8
class Nstr:
    def __init__(self,a,b):
        if isinstance(a,str):
            self.a = a
        if isinstance(b,str):
            self.b = b
    def sub(self):
        if self.a in self.b:
            return self.b.replace(self.a,'')

a = Nstr('i','I love youiiiiii')
print(a.sub())
