# 编写一个程序,用户输入文件名以及开始搜索的路径,搜索该文件是否存在.如遇到文件夹，则进入文件夹继续搜索,程序实现如图:
# -*- coding:utf8 -*-
import os
import os.path
init_dir = input('请输入待查找的初始目录:')
file_name = input('请输入需要查找的目标文件:')

def search_dir(init_dir,file_name):
    files = os.listdir(init_dir)
    for each in files:
        if os.path.isfile(init_dir+'\\'+ each) and file_name == each:
            print(init_dir+'\\'+ each)
        if os.path.isdir(init_dir+'\\'+ each):
            init_dir = init_dir + '\\' + each
            search_dir(init_dir,file_name)
            os.chdir(os.pardir)

search_dir(init_dir,file_name)




