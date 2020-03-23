#2.编写一个将十进制转换为二进制的函数,要求采用"除 2取余"(脑补链接)的方式,
# 结果与调用bin()一样返回字符串形式。
def binary(x):
    temp=list()
    while x//2:
        temp.append(x % 2)
        x = x//2
        if x == 1:
            temp.append(x % 2)
            break
    temp.reverse()
    s=''
    for i in temp:
        s+=str(i)
    return s
print(binary(62))