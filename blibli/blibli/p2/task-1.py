#1. 编写程序：calc.py 要求用户输入1到100之间数字并判断，输入符合要求打印“你妹好漂亮”，不符合要求则打印“你大爷好丑”
temp = input('请输入数字1-200:')
numb = int(temp)
if 1<= numb <= 100:
    print('你妹好漂亮')
else:
    print('你大爷好丑')