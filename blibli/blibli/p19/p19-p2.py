#2.编写一个函数findstr(),该函数统计一个长度为2的子字符串在另一个字符串中出现的次数.
# 例如:假定输入的字符串为"You cannot improve your past,but you can improve your future.
# Once time is wasted,life is wasted.",子字符串为"im",函数执行后打印"子字母串在目标字符串
# 中共出现3次".
def findstr():
    umstr = input('请输入目标字符串:')
    print('\n')
    secondstr=input('请输入子字符串(两个字符):')
    times = umstr.count(secondstr)
    print('子字符串在目标字符串中共出现 ',times,' 次')

findstr()
