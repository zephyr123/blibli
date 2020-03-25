# 2.还记得求回文字符串那道题吗？现在让你使用递归的方式来求解，亲还能骄傲的说我可以吗？
list1=[]
def fab(string):
    if len(string):
        list1.append(list(string).pop())
        del list(string)[-1]
        fab(string)
    print(string)
    exit()
    if list1 == list(string):
        print('是回文字符串')
    else:
        print('不是回文字符串')
fab('上海自来水来自海上')
