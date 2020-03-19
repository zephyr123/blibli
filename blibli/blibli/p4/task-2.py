temp = input('请输入一个整数:')
number = int(temp)
str = '*'
space = ' '
while number:
    print(space * number + str * number)
    number -= 1
