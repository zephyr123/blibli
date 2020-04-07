#-*- coding:utf8 -*-
class C:
    def __init__(self,x=0):
        self.x = x

c1 = C()
print(setattr(c1,'y','FishC'))
print(c1.y)