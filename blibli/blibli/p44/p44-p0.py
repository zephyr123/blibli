#coding:utf8
class A:
    def __init__(self,*args):
        if len(args) == 0:
            print('并没有传出参数')
        elif len(args) >= 1:
            print('传出了' + str(len(args)) + '个参数.分别是:',end=' ')
            for i in args:
                print(i,end=' ')


a = A()
b = A(1,'a','hello')
