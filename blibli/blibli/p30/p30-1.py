'''
任务:将文件(record.txt)中的数据进行分割并按照以下规律保存起来:
- 小甲鱼的对话单独保存为boy_*.txt的文件(去掉"小甲鱼:")
- 小客服的对话单独保存为girl_*.txt的文件(去掉"小客服:")
- 文件中总共有三段对话,分别保存为boy_1.txt,girl_1.txt,boy_2.txt,gir_2.txt,boy_3.txt,girl_3.txt
共6个文件(提示:文件中不同的对话间已经使用"======="分割)
'''
f=open('F:\\python_work\\blibli\\blibli\\p30\\record.txt','r',encoding='utf8')
file_dir = 'F:\\python_work\\blibli\\blibli\\p30\\'
count = 1
for each_line in f:
    if '======' in each_line:
        count += 1
    boy_file = 'boy_' + str(count) +'.txt'
    girl_file = 'girl_' + str(count) + '.txt'
    boy_files= open( file_dir + boy_file,'a+')
    girl_files = open( file_dir + girl_file,'a+')
    if '小客服' in each_line:
        girl_files.write(each_line.split(':')[1])
    elif '小甲鱼' in each_line:
        boy_files.write(each_line.split(':')[1])


