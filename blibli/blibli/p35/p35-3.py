#-*- coding:utf8 -*-
try:
    f = open('f:\\data.txt','w')
    for each_line in f:
        print(each_line)
except OSError as reason:
    print('出错啦:'+str(reason))
finally:
    f.close()