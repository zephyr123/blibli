f1=open('d:\\openme.mp3','r',encoding='utf8')
f2=open('d:\\openme.txt','x')  #使用‘x’打开更安全
f2.write(f1.read())
f2.close()
f1.close()
