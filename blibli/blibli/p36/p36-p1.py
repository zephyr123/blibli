#-*- coding:utf8 -*-
import easygui as g
import sys

list = ['用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
msg='【*真实姓名】为必填项\n【*手机号码】为必填项\n【*E-mail】为必填项'
title = '账号中心'
flag = 0
while True:
    Info = g.multenterbox(msg,title,fields=(list))
    for i in list:
        if '*' in i and Info[list.index(i)] == '':
            g.msgbox('带*为必填项,不能为空!!1')
            break
    else:
        g.msgbox('恭喜您,填写完成！')
        sys.exit()



