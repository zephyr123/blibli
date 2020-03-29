# 1.编写一个程序，比较用户输入的两个文件，如果不同，显示所有不同处的行号与第一个不同字符的位置，程序实现如图：
#-*- coding:UTF8 -*-
dir = 'F:\\python_work\\blibli\\blibli\\p30\\'
filename1 = input('请输入需要比较的头一个文件名:')
filename2 = input('请输入需要比较的另一个文件名:')
file1 = open(dir + filename1,'r')
file2 = open(dir + filename2,'r')

def diff_file(file1,file2,count=0):
    file1_list = []
    for each_line in file1:
        file1_list.append(each_line)
    for each_line in file2:
        if each_line != file1_list[count]:
            print('第' + str(count+1) +'行不一样')
        count +=1

diff_file(file1,file2)
