#0.编写一个函数,判断传入的字符串参数是否为"回文联"(回文联即用回文形式携程的对联，
# 既可倒读，例如,上海自来水来自海上)
def backFederation(startStr):
    backStr=''
    list1=list(startStr)
    length=len(list1)
    while length:
        backStr += list1.pop()
        length-=1
    if backStr == startStr:
        print('是回文联')
    else:
        print('不是回文联')

String=input('请输入一句话:')
backFederation(String)

