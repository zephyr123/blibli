# 1.寻找水仙花数
# 题目要求:如果一个三位数等于其三位数字的立方和，则成为这个数为水仙花数。例如
# 153 = 1^3 + 5^3 + 3^3,因此153是一个水仙花数，编写一个程序,找出所有水仙花数。


for i in range(100,1000):
    temp = i
    sum = 0
    while temp:
        sum += (temp % 10)**3
        temp = temp // 10
    if i == sum:
        print(i)