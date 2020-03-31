# 编写一个程序,计算当前文件夹下所有文件的大小,程序试下如图:
# -*- coding:utf8 -*-
import os
import os.path
all_files = os.listdir(os.curdir)
for each_file in all_files:
    if os.path.isfile(each_file):
        size = os.path.getsize(each_file)
        print(each_file,'【%s】'% size)

