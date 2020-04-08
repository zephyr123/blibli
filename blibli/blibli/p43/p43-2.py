# coding:utf8
class Try_int(int):
    def __add__(self, other):
        return int(self) + int(other)

    def __sub__(self, other):
        return int(self) - int(other)


a = Try_int(3)
b = Try_int(5)
print(a - b)
