#-*- coding:utf8 -*-
class C:
    def __init__(self,x=0):
        self.x = x

c1 = C()
print(hasattr(c1,'x'))
print(hasattr(c1,'y'))
print(getattr(c1,'x'))
# print(getattr(c1,'y'))
print(getattr(c1,'y','您所访问的参数不存在'))