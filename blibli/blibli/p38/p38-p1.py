#-*- coding:utf8 -*-
import random as r

legal_x = [0,10]
legal_y = [0,10]

class Turtle:
    def __init__(self):
        #初始体力
        self.power = 100
        #初始位置
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        #随机计算方向并生成新的位置
        new_x = self.x + r.choice([1,2,-1,-2])
        new_y = self.y + r.choice([1,2,-1,-2])
        #判断是否碰到x边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        #判断是否碰到y的边界
        if new_y < legal_y[0]:
            new_y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            new_y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        self.power -= 1
        return (self.x,self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish:
    def __init__(self):
        #初始位置
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        new_x = self.x + r.choice([1,-1])
        new_y = self.y + r.choice([1,-1])
        #判断是否到x边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        #判断是否碰到y边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        #返回移动后的新位置
        return (self.x,self.y)

turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼儿被吃完了,游戏结束!")
        break
    if not turtle.power:
        print("乌龟体力耗尽，挂掉了!")
        break
    pos = turtle.move()
    for each_fish in fish[:]:
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼儿被吃掉了!")




