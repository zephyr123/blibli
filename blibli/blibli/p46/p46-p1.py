#coding:utf8
class Demo:
    def __init__(self,x='FishC'):
        self.x = x
    def __setattr__(self, x, value):
        return super().__setattr__(x,value)

demo = Demo()
print(demo.x)
demo.x = 'X-man'
print(demo.x)
