password = 'fishC123'
userpasswd = input('请输入您的密码:')
i = 0
j = '*'
while i<2:
    if userpasswd == password:
        print('恭喜您，密码正确!')
        break
    else:
        for j in userpasswd:
            continue
        userpasswd = input('输错了,请重新输入您的密码:')
        i+=1
