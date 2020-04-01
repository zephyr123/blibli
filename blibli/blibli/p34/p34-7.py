#-*- coding:utf8 -*-
try:
    f = open('f:\\怎么样.txt','w')
    print(f.write('我存在了！'))
    sum = 1 + '1'

except (OSError,TypeError):
    print('出错啦!')
finally:
    f.close()