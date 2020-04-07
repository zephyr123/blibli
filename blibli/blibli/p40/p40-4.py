#-*- coding:utf8 -*-
class CC:
    def setYY(self,x,y):
        self.x = x
        self.y = y

    def printXY(self):
        print(self.x,self.y)

dd = CC()
print(dd.__dict__)
print(CC.__dict__)
del CC
ee = CC()