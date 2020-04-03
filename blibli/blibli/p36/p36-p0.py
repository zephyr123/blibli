#-*- coding:utf8 -*-
import random
import easygui as g
secret = random.randint(0,10)
guess = g.integerbox('请猜猜小甲鱼心中的数字(1-10):', lowerbound='0', upperbound='10')
while True:
    if guess == secret:
        g.msgbox('恭喜你输入正确！')
        break
    elif guess > secret:
        guess = g.integerbox('大了，大了,请重新输入:', lowerbound='0', upperbound='10')
    elif guess < secret:
        guess = g.integerbox('小啦,请重新输入:', lowerbound='0', upperbound='10')