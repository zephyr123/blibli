#要求在上一题的基础上扩展，用户可以随意输入显示的行数。如输入13:21,打印第13行到第21行，输入：21打印前21行，输入21：则打印从21行开始到文件结尾所有内容
#-*- coding:UTF8 -*-
dir = 'F:\\python_work\\blibli\\blibli\\p30\\'
file_name = input('请输入要打开的文件:')
lines = input('请输入要显示的行数:')
file = open(dir + file_name,'r')
file_list = list(file.readlines())
(start,end)=lines.split(':')
if start == '':
    start = 0
else:
    start = int(start) - 1
if end == '':
    end = len(file_list)
else:
    end = int(end)

for temp in range(start,end):
    print(file_list[temp],end='')

file.close()