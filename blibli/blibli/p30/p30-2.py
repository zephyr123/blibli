# -*- coding: UTF-8 -*-
f = open('F:\\python_work\\blibli\\blibli\\p30\\record.txt','r',encoding='utf8')
dir = 'F:\\python_work\\blibli\\blibli\\p30\\'
boy = []
girl = []
count = 1
for each_line in f:
    if each_line[:6] != '======':
        (role,line_spoken) = each_line.split(':',1)
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_spoken)
    else:
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'
        boy_file = open(dir + file_name_boy,'w')
        girl_file = open(dir + file_name_girl,'w')
        boy_file.writelines(boy)
        girl_file.writelines(girl)
        boy_file.close()
        girl_file.close()
        boy = []
        girl = []
        count +=1


file_name_boy = 'boy_' + str(count) + '.txt'
file_name_girl = 'girl_' + str(count) + '.txt'
boy_file = open(dir + file_name_boy,'w')
girl_file = open(dir + file_name_girl,'w')
boy_file.writelines(boy)
girl_file.writelines(girl)
boy_file.close()
girl_file.close()
boy = []
girl = []
count +=1
f.close()