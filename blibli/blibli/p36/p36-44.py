#-*- coding:utf8 -*-
import easygui as g
import os

def show_result(start_dir):
    lines = 0
    total = 0
    text = ""

    for i in source_list:
        lines = source_list[i]
        total += lines
        text +="【%s】源文件%d个,源代码%d行\n" % (i,file_list[i],lines)
    title = '统计结果'
    msg = '您目前累计编写了%d行代码,完成进度:%.2f %%\n离 10万行代码还差%d行,请继续努力!' %(total,total/10000,10000-total)
    g.textbox(msg,title,text)

def calc_code(file_name):
    lines = 0
    with open(file_name,encoding='utf-8') as f:
        print('正在分析文件:%s...' % file_name)
        try:
            for each_line in f:
                lines += 1
        except UnicodeDecodeError:
            pass #不可避免会遇到格式不兼容的文件,这里忽略掉...
    # print(lines);print(file_name);print(os.getcwd());exit()
    return lines

def search_file(start_dir):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            lines = calc_code(each_file) #统计行数
            #还记得异常的用法吗?如果字典不存在,抛出KeyError,则添加字典键
            #统计文件数
            try:
                file_list[ext] +=1
            except KeyError:
                file_list[ext] = 1
            #统计源代码行数
            try:
                source_list[ext] += lines
            except KeyError:
                source_list[ext] = lines

        if os.path.isdir(each_file):
            search_file(each_file) #递归调用
            os.chdir(os.pardir) #递归调用后切记返回上一层目录

target = ['.c','.cpp','.py','.cc','.java','.pas','.asm']
file_list = {}
source_list = {}

g.msgbox("请打开您存放所有代码的文件夹......",'统计代码量')
path = g.diropenbox("请选择您的代码库:")

search_file(path)
show_result(path)
