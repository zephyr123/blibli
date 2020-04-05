#-*- coding:utf8 -*-
import math
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    def getY(self):
        return self.y

class Line():
    def __init__(self,p1,p2):
        self.x = p2.getX() - p1.getX()
        self.y = p2.getY() - p2.getY()
        self.length = math.sqrt(self.x * self.x + self.y * self.y)

    def getLength(self):
        return self.length

p1 = Point(1,1)
p2 = Point(4,5)
long = Line(p1,p2)
print(long.getLength())



