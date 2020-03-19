import os
import os.path
filenames = os.listdir('F:\\p30\\1_dir')
dirname = 'F:\\p30\\1_dir\\'
for filename in filenames:
    #print(filename)
    pwd = dirname + filename
    # print(pwd)
    print(filename + ' [' + str(os.path.getsize(pwd)) + 'Bytes]')