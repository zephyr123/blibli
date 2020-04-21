#coding:utf8
def myGen():
    print("生成器被执行!")
    yield 1
    yield 2

myG = myGen()
print(next(myG))
# print(next(myG))
# next(myG)