#coding:utf8
class A:
    def __getattr__(self,name):
        print('该属性不存在!')

a = A()
print(a.x)