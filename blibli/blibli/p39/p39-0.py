#-*- coding:utf8 -*-
class Parent:
    def hello(self):
        print("正在调用父类的方法...")


class Child(Parent):
    pass


class MyClass:
    def __init__(self):
        return "I love FishiC.com"

a = MyClass()
p = Parent()
p.hello()
c = Child()
c.hello()
