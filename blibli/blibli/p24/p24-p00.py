#0.使用递归编写一个十进制转换为二进制的函数(要求采用“取2取余”的方式,
# 结果与调用bin()一样返回字符串形式)
def DecToBin(dec):
    result = ''
    if dec:
        result = DecToBin(dec//2)
        return result + str(dec%2)
    else:
        return result

print(DecToBin(10))

