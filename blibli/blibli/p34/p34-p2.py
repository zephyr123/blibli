#-*- coding:utf8 -*-
number = input('请输入一个整数:')
def int_input(number):
    try:
        # number = int(number)
        if isinstance(number,int):
            print('输入正常')
        elif isinstance(number,str):
            print('输入的不是整数,请重新输入:')
            number=input()
            int_input(number)
    except:
        number = input('输入的不是整数,请重新输入:')


int_input(number)
