#coding:utf8
class MyDes:
    def __get__(self, instance, owner):
        print("getting...")

class Test:
    a = MyDes()
    x = a

test = Test()

