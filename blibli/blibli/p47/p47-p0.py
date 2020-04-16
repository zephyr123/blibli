#coding:utf8
class Mydes:
    def __init__(self,initval=None,name=None):
        self.val = initval
        self.name = name
    def __get__(self, instance, owner):
        print("正在获取变量:",self.name)
        return self.val
    def __set__(self, instance, value):
        print("正在修改变量:",self.name)
        self.val = value
    def __delete__(self, instance):
        print("正在删除变量:",self.name)
        print("嗷~这个变量没法删除~")

class Test:
    x = Mydes(10,'x')

test = Test()
y = test.x
print(y)
test.x = 8
del test.x
print(test.x)




