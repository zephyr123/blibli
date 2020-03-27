import random
times = 3
secret = random.randint(1,10)
#这里先给secret赋值，赋值一个肯定不等于secret的值
guess = 0
#print()默认打印完字符串会自动添加一个换行符,end=""告诉print()用空格代替换行符
print("不妨猜下小甲鱼心里想的哪个数字:  ",end="")
while (guess != secret) and (times > 0):
    temp = input()
    while not temp.isdigit():
        temp = input('抱歉，请输入一个整数:')
    guess = int(temp)
    times = times -1
    if guess == secret:
        print('猜对了!')
        print('哼，猜对了也没奖励！')
    else:
        if guess > secret:
            print('大了,大了！')
        else:
            print('嘿，小了！')
        if times > 0:
            print('再试一次吧:',end="")
        else:
            print("机会用光了！")
print('游戏结束,不玩啦')
