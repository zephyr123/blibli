# 1.请用已学过的只是编写程序，找到小甲鱼藏在这个长字符串中的密码，密码的埋藏点符合以下规律：
# a)每位密码为单个小写字母
# b)每位密码的左右两边均有且只有三个大写字母
str1 = '''拷贝过来的字符串'''
countA = 0
countB = 0
countC = 0
length = len(str1)
for i in range(length):
    if str1[i] == '\n':
        continue
    if str1[i].isupper():
        if countB == 1:
            countC += 1
            countA = 0
        else:
            countA += 1
        continue
    if str1[i].islower() and countA == 3:
        countB = 1
        countA = 0
        target = i
        continue
    if str1[i].islower() and countC == 1:
        print(str1[target],end='')
    countA = 0
    countB = 0
    countC = 0





