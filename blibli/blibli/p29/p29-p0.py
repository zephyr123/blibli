# 0.尝试将文件 OpenMe.mp3，打印到屏幕上
f=open('d:\\openme.mp3','r',encoding='utf8')
for each_line in f:
    print(each_line,end='')
f.close()