#-*- coding:utf8 -*-
try:
    sum = 1 + '1'
    f = open('f:\\怎么样.txt')
    print(f.read())
    f.close()
except (OSError,TypeError):
    print('出错啦!')