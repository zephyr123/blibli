#0.使用递归编写一个十进制转换为二进制的函数(要求采用“取2取余”的方式,
# 结果与调用bin()一样返回字符串形式)
def DecToBin(x):
    while x:
        list1.append(x%2)
        x = x // 2
    list1.reverse()
    return list1


list1 = list()
print(DecToBin(10))