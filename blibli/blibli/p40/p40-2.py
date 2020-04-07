#-*- coding:utf8 -*-
class C:
    def x(self):
        print("X-manx!")

c = C()
c.x()
c.x = 1
print(c.x)
c.x()
