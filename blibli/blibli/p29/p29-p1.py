# 1.编写代码,将上一题中的文件(OpenMe.mp3)保存为新文件(OpenMe.txt)
f=open('d:\\openme.mp3','r',encoding='utf8')
f1=open('d:\\openme.txt','w+')
for each_line in f:
    f1.write(each_line)
    f1.write('\n')

f.close()
f1.close()