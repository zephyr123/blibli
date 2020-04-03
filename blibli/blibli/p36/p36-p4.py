#-*- coding:utf8 -*-
import easygui as g
import os
import os.path

def file_lines(file):
    global line_count
    with open(file,'r',encoding='UTF-8') as f:
        number = len(f.readlines())
        line_count += number
        # return line_count

def search_file(dir):
    global py_count
    os.chdir(dir)
    for each_file in os.listdir(os.curdir):
        if os.path.isfile(each_file):
            (role,spoken) = os.path.splitext(each_file)
            if spoken == '.py':
                py_count += 1
                file_pwd = os.getcwd() + os.sep + each_file
                file_lines(file_pwd)
        if os.path.isdir(each_file):
            search_file(each_file)
            os.chdir(os.pardir)


dir = g.diropenbox()
py_count = 0
line_count = 0
search_file(dir)
print('【%s】源文件%d个，源代码%d行'%(spoken,py_count,line_count))


