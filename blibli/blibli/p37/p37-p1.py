#-*- coding:utf8 -*-
class Rectangle:
    length = 5
    width = 4

    def getRect(self):
        print('这个矩形的长是:' + str(self.length) + ',宽是:' + str(self.width))

    def setRect(self):
        print('请输入矩形的长和宽')
        self.length = input('长:')
        self.width = input('宽:')

    def getArea(self):
        print(float(self.length) * float(self.width))

juxing = Rectangle()
juxing.getRect()
juxing.setRect()
juxing.getArea()