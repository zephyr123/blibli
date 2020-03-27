'''
#0.请写一个密码安全性检查的脚本代码: check.py
#密码安全性检查代码
#低级密码要求
#1.密码由单纯的数字或字母组成
#2.密码长度小于等于8位
#中级密码要求:
#1.密码必须由数字、字母或特殊字符(仅限:)任意两种组合
#2.密码长度不能低于8位
#高级密码要求:
#1.密码必须由数字、字母及特殊字符(仅限)三种组合
#2.密码只能由字母开头。
#3.密码长度不能低于16位
'''
import re
password=input('请输入您的密码:')
if len(password)<=8 and (password.isalpha() or password.isdigit()):
        print('符合低级密码要求!')
elif 16 > len(password) > 8:
    if bool(re.findall('[a-zA-Z]',password)) and bool(re.findall('\d',password)):
        print('符合中级密码要求!')
    elif bool(re.findall('[a-zA-Z]',password)) and bool(re.findall('\W',password)):
        print('符合中级密码要求!')
    elif bool(re.findall('\d',password)) and bool(re.findall('\W',password)):
        print('符合中级密码要求!')
    else:
        print('不密码不符合中级密码要求！')
elif len(password) >=16 and password[0].isalpha and bool(re.findall('\d',password)) and bool(re.findall('\W',password)) and bool(re.findall('[a-zA-Z]',password)):
    print('符合高级密码要求!')
else:
    print('不符合密码任何级别的密码要求!')
