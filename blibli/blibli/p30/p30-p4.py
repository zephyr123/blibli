#替换单词或字符
#-*- coding:UTF8 -*-
dir = 'F:\\python_work\\blibli\\blibli\\p30\\'
file_name = input('请输入文件名:')
word1 = input('请输入需要替换的单词或字符:')
word2 = input('请输入新的单词或字符:')
file = open(dir+file_name,'r')
string = file.read()
count = string.count(word1)
file.close()
file = open(dir+file_name,'w')
print('文件' + file_name + '中共共有' + str(count) + '个'+ word1+',你确定要把所有的' + word1 +
      '替换为' + word2 +'吗?')
que = input('【YES/NO】')
if que == 'YES' or que == 'yes':
    file.write(string.replace(word1,word2))
file.close()



