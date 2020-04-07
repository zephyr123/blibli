#-*- coding:utf8 -*-
class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self,x,y):
        self.trutle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("水池里总共有乌龟%d只,小鱼%d条!" %(self.trutle.num,self.fish.num))

pool = Pool(1,10)
pool.print_num()