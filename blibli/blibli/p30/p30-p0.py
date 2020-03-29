# 0.编写一个程序，接受用户的输入并保持为新的文件，程序实现如图
#-*- coding:UTF8 -*-
filename = input('请输入文件名:')
content = input('请输入文件内容[单独输入:w保存退出]：')
dir = 'F:\\python_work\\blibli\\blibli\\p30\\'
file = open(dir+filename,'w')
def save_file(content,file):
    while True:
        content = input()
        if content == ':w':
            break
        else:
            file.write(content)
            file.write('\n')
    file.close()

save_file(content,file)


