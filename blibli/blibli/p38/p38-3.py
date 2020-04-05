#-*- coding:utf8 -*-
class Person:
    __name = '小甲鱼'

    def getName(self):
        return self.__name

p = Person()
print(p.getName())
print(p._Person__name)
