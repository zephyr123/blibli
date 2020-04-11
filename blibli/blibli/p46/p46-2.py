#coding:utf8
class C:
    def __getattribute__(self, name):
        print('getattribute')  #首先被访问
        return super().__getattribute__(name)
    def __getattr__(self, name): #不存在时被访问
        print('getattr')
    def __setattr__(self, name, value):
        print('setattr')
        super().__setattr__(name,value)
    def __delattr__(self, item):
        print('delattr')
        super().__delattr__(name)

c = C()
print(c.x)
c.x = 1
print(c.x)
del c.x