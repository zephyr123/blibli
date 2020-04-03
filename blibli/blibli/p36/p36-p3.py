#-*- coding:utf8 -*-
import easygui as g
file=g.fileopenbox('请选择需要打开的文本文件',default='*.txt',filetypes=["*.txt"])
f = open(file,'r+')
list1 = f.read()
list = g.textbox('要打开的文本文件内容如下:',text=open(file,'r+'))

if list:
    if list == list1:
        print('文件没有改变')
    else:
        select = g.buttonbox('监测到文件已经改变，请选择一下操作','警告', choices=('覆盖保存', '放弃保存', '另存为'))
        if select == '覆盖保存':
            with open(file,'w') as f1:
                f1.write(list)
        if select == '放弃保存':
            pass
        elif select == '另存为':
            anther_file = g.filesavebox(default='.txt')
            with open(anther_file,'w') as new_file:
                new_file.write(list)

