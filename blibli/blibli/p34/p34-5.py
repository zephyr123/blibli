#-*- coding:utf8 -*-
try:
    sum = 1 + '1'
    f = open('f:\\readme.txt')
    print(f.read())
    f.close()
except:
    print('出错啦!')
