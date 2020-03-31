# -*- coding:utf8 -*-
import os
import os.path
start_dir = input('请输入待查找的初始目录:')
dir_lsit = []
def search_mv(start_dir):
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):
        if os.path.isfile(each_file):
            ext = os.path.splitext(each_file)[1]
            if ext n ['.mp4','.rmvb','.avi']:
                dir_lsit.append(os.getcwd() + os.sep + each_file)
        if os.path.isdir(each_file):
            search_mv(each_file)
            os.chdir(os.pardir)

search_mv(start_dir)
f = open('F:\\python_work\\blibli\\blibli\\p31\\vedioList.txt','w')
for file in dir_lsit:
    f.write('%s\n'%file)
f.close()