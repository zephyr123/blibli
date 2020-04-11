#coding:utf8
class Counter:
    def __init__(self):
        self.counter = 0 #这里会触发__setattr__调用
    def __setattr__(self, name, value):
        self.counter += 1
'''既然需要__setattr__调用后才能真正设置self.counter的值,所以这时候self.counter还没有定义,所以设法+=1，错误根源'''
        super().__setattr__(name,value)
    def __delattr__(self,name):
        self.counter -= 1
        super().__delattr__(name)
