#-*- coding:utf8 -*-
class Ball:
    def setName(self,name):
        self.name = name

    def kick(self):
        print("我叫%s,该死的,谁踢我..."% self.name)

a = Ball()
a.setName('球A')
a.kick()
b = Ball()
b.setName('球B')
b.kick()
c = Ball()
c.setName('土豆')
c.kick()