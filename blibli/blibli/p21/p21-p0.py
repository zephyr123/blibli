#0.请用已学过的知识编写程序，统计下边这个长字符串中各个字符出现的次数并找到小甲鱼送给大家的一句话
str1 = '''拷贝过来的字符串'''
list1 = []
for each in str1:
    if each not in list1:
        if each == '\n':
            print('\\n',str1.count(each))
        else:
            print(each,str1.count(each))
        list1.append(each)
