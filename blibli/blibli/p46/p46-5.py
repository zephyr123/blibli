#coding:utf8
class Counter:
    counter = 0
    def __init__(self):
        self.counter = 0
    def __setattr__(self, name, value):
        # self.counter += 1
        Counter.counter += 1
        super().__setattr__(name,value)
    def __delattr__(self, name):
        # self.counter -=1
        Counter.counter -= 1
        super().__delattr__(name)
c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.counter)
del c1.counter
print(Counter.counter)

