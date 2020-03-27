import os
import os.path
filedir = input('请输入开始搜索的路径:')
filename = input('请输入用户输入文件名:')
file = filedir +'\\' + filename
# print(file)
if os.path.isfile(file):
    print(file)

