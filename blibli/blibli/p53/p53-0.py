#coding:utf8
class A:
    def __init__(self):
        pass
    def get(self):
        print(__name__)
a = A()
a.get()