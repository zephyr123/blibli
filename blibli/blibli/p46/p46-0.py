#coding:utf8
class C:
    def __init__(self):
        self.x = 'X-man'

c = C()
print(c.x)
print(getattr(c,'x','木有这个属性!'))
print(getattr(c,'y','木有这个属性!'))
