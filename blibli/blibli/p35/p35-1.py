#-*- coding:utf8 -*-
try:
    int('1')
except ValueError as reason:
    print('出错啦:' + str(reason))
else:
    print('没有任何异常')
