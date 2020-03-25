#0.使用递归编写一个power()函数模拟内建函数pow()，即power(x,y)为计算并返回x的y次幂的值。
def power(x,y):
    result = 0
    if y == 1:
        return x
    else:
        return  x * power(x,y-1)

print(power(5,2))
