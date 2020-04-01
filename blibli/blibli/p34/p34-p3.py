#-*- coding:utf8 -*-
try:
    f = open('F:\\python_work\\blibli\\blibli\\p34\\My_file.txt') #当前文件夹中并不存在"My_file.txt"这个文件
    print(f.read())
except OSError as reason:
    print('出错啦:' + str(reason))
finally:
    f.close()
