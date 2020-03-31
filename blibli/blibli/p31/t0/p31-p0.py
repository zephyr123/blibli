# 编写一个程序,统计当前目录下每个文件类型的文件数,程序实现如图
# -*- coding:utf8 -*-
import os
import os.path
all_files = os.listdir(os.curdir)
type_dict = {}
print(all_files)
for each in all_files:
    if os.path.isdir(each):
        type_dict.setdefault('文件夹',0)
        type_dict['文件夹'] +=1
    else:
        ext = os.path.splitext(each)[1]
        type_dict.setdefault(ext,0)
        type_dict[ext] +=1

for each_type in type_dict.keys():
    print('该文件夹中共有类型为【%s】的文件%d个'%(each_type,type_dict[each_type]))
