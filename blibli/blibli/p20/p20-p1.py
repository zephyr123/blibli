# 1.编写一个函数,分别统计出传入字符串参数(可能不只是一个参数)的英文字母、空格、数字和其他字符的个数.
def para(*params):
    alpha='abcdefghijklmnopqrstuvwxyzABCEFGHIJKLMNOPQRSTUVWXYZ'
    digit='1234567890'
    symbolic = r'~`!@#$%^&*()_+-=[]{}\|:;/<>?'
    space=' '
    for each in params:
        a=0
        b=0
        c=0
        d=0
        for i in each:
            if i in alpha:
                a+=1
            elif i in digit:
                b+=1
            elif i in space:
                c+=1
            elif i in symbolic:
                d+=1
        print(each + '该参数英文字母有:',a)
        print(each + '该参数数字有:', b)
        print(each + '该参数空格有:', c)
        print(each + '该参数有其他字符:', d)

para('abc','123&abcde','adsdls&*()2345  ')