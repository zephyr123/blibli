#1.编写一个函数,利用欧几里得算法(脑补链接)求最大公约数,
# 例如 gcd(x,y)返回值为参数x和参数y的最大公约数。
def gcd(x,y):
    if y == 0:
        return x
    return gcd(x,x%y)

print(gcd(2,3))