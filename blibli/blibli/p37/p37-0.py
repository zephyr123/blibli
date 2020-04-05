#-*- coding:utf8 -*-
class Turtle: #Ptyhon中的类名约定以答谢字母开头
    '''关于类的简单例子'''
    #属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'
    #方法
    def climb(self):
        print('我正在很努力的向前爬...')

    def run(self):
        print("我正在飞快的向前爬......")

    def bite(self):
        print("咬死你咬死你!")

    def eat(self):
        print('有得吃,真满足^_^')

    def sleep(self):
        print('困了,睡了,晚安,Zzzz')


Turtle() #实例化对象，又释放了
tt = Turtle() #实例化，赋值到了tt
tt.climb() #调用tt的climb()方法
tt.bite() #调用tt的bite()方法
