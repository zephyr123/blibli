# 2.编写一个程序，当用户输入文件名和行数(N)后，将该文件的前N行内容打印到屏幕上，程序实现如图：
#-*- coding:UTF8 -*-
dir = 'F:\\python_work\\blibli\\blibli\\p30\\'
file_name = input('请输入要打开的文件:')
lines = int(input('请输入要显示的行数:'))
file = open(dir + file_name,'r')
file_list = list(file.readlines())

for each_line in file_list:
    if lines != 0:
        print(each_line,end='')
    else:
        break
    lines-=1

file.close()



