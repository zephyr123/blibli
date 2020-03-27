import os
import os.path
filenames = os.listdir('f:\\p30\\0_dir')
# print(filenames)
list = []
i = 0
for each_filename in filenames:
    file = os.path.splitext(each_filename)
    for item in file:
        list.append(item)
#print(list)
print('该文件夹下共有类型为[.txt]的文件'+ str(list.count('.txt')) + '个')
print('该文件夹下共有类型为[.png]的文件'+ str(list.count('.png')) + '个')
print('该文件夹下共有类型为[.py]的文件'+ str(list.count('.py')) + '个')
print('该文件夹下共有类型为[.docx]的文件'+ str(list.count('.docx')) + '个')
print('该文件夹下共有类型为[文件夹]的文件'+ str(list.count('')) + '个')
    #
    # if file[1] == '.txt':
    #     i += 1
    #     print('该文件夹下共有类型为[.txt]的文件'+ str(i) + '个')
    #
    # elif file[1] == '.png':
    #     i = 0
    #     i += 1
    #     print('该文件夹下共有类型为[.png]的文件'+ str(i) + '个')
    # elif file[1] == '.py':
    #     i = 0
    #     i += 1
    #     print('该文件夹下共有类型为[.py]的文件'+ str(i) + '个')
    #
    # elif file[1] == '.docx':
    #     i = 0
    #     i += 1
    #     print('该文件夹下共有类型为[.docx]的文件'+ str(i) + '个')
    # else:
    #     i = 0
    #     i += 1
    #     print('该文件夹下共有类型为[文件夹]的文件' + str(i) + '个')