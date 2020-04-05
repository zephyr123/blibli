#-*- coding:utf8 -*-
class Parent:
    def hello(self):
        print("正在调用父类的方法...")


class Child(Parent):
    def hello(self):
        print("child自己的方法")

p = Parent()
p.hello()
c = Child()
c.hello()