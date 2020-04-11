#coding:utf8
class Counter:
    counter = 0
    def __setattr__(self, name, value):
        Counter.counter += 1
        super().__setattr__(name,value)
    def __delattr__(self, name):
        Counter.counter -=1
        super().__delattr__(name)
c = Counter()
c.x = 1
c.y = 1
c.z = 1
print(c.counter)
del c.x
print(c.counter)
