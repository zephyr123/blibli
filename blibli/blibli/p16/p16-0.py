#编写一个进制转换程序,程序演示如下(提示,十进制转换二进制可以用bin()
q = True
while q:
    temp = input('请输入一个整数:')
    #print('您的输入有误,请输入一个整数:', end='')
    if str(temp).isdigit():
        temp = int(temp)
        print(temp,'转换为八进制为:','%o' % temp)
        print(temp, '转换为十六进制为:', '%x' % temp)
        print(temp, '转换为二进制为:', bin(temp))
    elif temp == 'q':
        q=False
