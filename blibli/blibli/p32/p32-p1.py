#-**- coding:utf8 -*-
import pickle
f = open('F:\\python_work\\blibli\\blibli\\p32\\record.txt','r',encoding='utf8')
dir = 'F:\\python_work\\blibli\\blibli\\p32\\'

boy_list = []
girl_list = []
count = 1
for each_line in f:
    if each_line.split(':')[0] == '小客服':
        girl_list.append(each_line.split(':')[1])
    elif each_line.split(':')[0] == '小甲鱼':
        boy_list.append(each_line.split(':')[1])
    elif each_line[:6] == '======':
        pickle_girlfile= open(dir+'girl_'+ str(count)+'.txt','wb')
        pickle_boyfile= open(dir+'boy_'+str(count)+'.txt','wb')
        pickle.dump(girl_list,pickle_girlfile)
        pickle.dump(boy_list,pickle_boyfile)
        girl_list = []
        boy_list = []
        count += 1

pickle_girlfile = open(dir + 'girl_' + str(count)+'.txt', 'wb')
pickle_boyfile = open(dir + 'boy_' + str(count)+'.txt', 'wb')
pickle.dump(girl_list, pickle_girlfile)
pickle.dump(boy_list, pickle_boyfile)





