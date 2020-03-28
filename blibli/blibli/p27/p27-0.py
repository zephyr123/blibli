def login():
    print('|---新建用户:N/n---|')
    print('|---登录账户:E/e---|')
    print('|---退出程序:Q/q---|')

    instruct = input('|---请输入指令代码:')
    if instruct == 'N' or instruct == 'n':
        name = input('请输入用户名:')
        if name not in username:
            username[name] = input('请输入密码:')
            print('注册成功,赶紧试试登录吧^_^')
        else:
            name = input('此用户名已经被使用,请重新输入:')
            username[name] = input('请输入密码:')
            print('注册成功,赶紧试试登录吧^_^')

    if instruct == 'E' or instruct == 'e':
        name = input('请输入用户名:')
        if name not in username:
            name = input('您输入的用户不存在,请重新输入:')
            password = input('请输入密码:')
            if username[name] == password:
                print('欢迎进入XXOO系统,请点击右上方的X结束程序')

    if instruct == 'Q' or instruct == 'q':
        exit()

username = {'小甲鱼':'123456'}
login()

