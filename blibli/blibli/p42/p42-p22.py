#coding:utf8
class Nint(int):
    def __new__(cls,arg=0):
        if isinstance(arg,str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        return int.__new__(cls,arg)

print(Nint('abc'))