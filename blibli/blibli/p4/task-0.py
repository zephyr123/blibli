i = 3
while i:
    temp = input('请输入数字:')
    number = int(temp)
    if number == 50:
        print('恭喜你!答对了！')
        exit()
    else:
        print('不好意思，您输错了')
    i-=1
