#1.编写一个程序,求100-999之间的所有水仙花数。
# 如果一个3位数等于其各位数字的立方和,则称这个数为水仙花数。
# 例如:153=1^3 + 5^3+ 3^3，因此153就是一个水仙花数。
number=100
while number <=999:
    temp = 0
    for i in str(number):
        temp += int(i)**3
    if number == temp:
        print(number)
    number+=1

