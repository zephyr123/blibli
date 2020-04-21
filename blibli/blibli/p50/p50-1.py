#coding:utf8
def myGen():
    print("生成器被执行!")
    yield 1
    yield 2

for i in myGen():
    print(i)