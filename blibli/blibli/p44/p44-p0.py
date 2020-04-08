#coding:utf8
class A:
    def __init__(self,*args):
        if len(args) == 0:
            print('并没有传出参数')
        elif len(args) >= 1:
            self.count = 0
            for i in args:
                self.count += 1
            print('传出了' + str(self.count) + '个参数.分别是' + str(args) )

a = A()
b = A(1,'a','hello')
