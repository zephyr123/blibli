#1.视频中我们说sum()这个BIF有个缺陷，就是如果参数里有字符串类型的话就会报错，请写出一个新的实现过程，
# 自动"无视"参数里的字符串并返回正确的计算结果。
numbers=input('请输入一个数字:')
temp=[]
for each in numbers:
    if  not each.isalpha():
        each = int(each)
        temp.append(each)
print(sum(temp))
