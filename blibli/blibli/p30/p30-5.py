import os
import os.path
file_dir = input('请输入要查找的路径:')
filenames = os.listdir(file_dir)
newfile=file_dir + '\\' + 'vedioList.txt'
f=open(newfile,'w')
for filename in filenames:
    if 'rmvb' in filename or 'avi' in filename or 'mp4' in filename:
        # print(filename)
        f.write(file_dir + '\\' + filename)
        f.write('\r\n')