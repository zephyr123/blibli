#-*- coding:utf8 -*-
class Stack:
    def __init__(self):
        self.list = list()

    def isEmpty(self):
        if len(self.list):
            return True
        else:
            return False

    def push(self,x):
        self.list.append(x)

    def pop(self):
        return self.list.pop()

    def top(self):
        print(self.list[-1])

    def bottom(self):
        print(self.list[0])

a = Stack()
print(a.isEmpty())
a.push(1)
a.push(3)
a.push(5)
a.pop()
a.top()
a.bottom()