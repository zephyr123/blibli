#-*- coding:utf8 -*-
import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,20)
        self.y = r.randint(0,20)

    def move(self):
        self.x -= 1
        print("我的位置是:",self.x,self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self)
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有的吃^_^")
            self.hungry = False
        else:
            print("太撑了,吃不下了!")

fish = Fish()
fish.move()
goldfish = Goldfish()
goldfish.move()
shark = Shark()
shark.eat()
shark.eat()
shark.move()