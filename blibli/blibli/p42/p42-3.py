#coding:utf8
class C:
    def __init__(self):
        print("我是__init__方法,我被调用了...")
    def __del__(self):
        print("我是__del__方法,我被调用了...")

c1 = C()
c2 = c1
c3 = c2
del c3
del c2
del c1