#0.编写一个符合以下要求的函数:
# a)计算打印所有参数的和乘以基数(base=3)的结果。
# b)如果参数中最后一个参数为(base=5),则设为基数为5,基数不参与求和计算。

def base(*params):
    result = 0
    if params[-1] != 5:
        for each in params:
            result +=each
        result = result*3
    else:
        for each in params:
            result += each
        result = (result - 5)*5
    return result

print(base(2,3,7,5))