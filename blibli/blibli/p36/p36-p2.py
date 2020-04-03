#-*- coding:utf8 -*-
import easygui as g
file=g.fileopenbox('请选择需要打开的文本文件',default='*.txt',filetypes=["*.txt"])
g.textbox('要打开的文本文件内容如下:',text=open(file,'r'))

