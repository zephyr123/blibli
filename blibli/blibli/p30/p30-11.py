def file_compare(file1,file2):
    f1 = open(file1)
    f2 = open(file2)
    count = 0 #ͳ������
    differ = [] #ͳ�Ʋ�һ��������

    for line1 in f1:
        line2 = f2.readline()
        count +=1
        if line1 !=line2:
            differ.append(count)
    f1.close()
    f2.close()
    return differ

file1 = input('��������Ҫ�Ƚϵ�ͷһ���ļ�:')
file2 = input('��������Ҫ�Ƚϵ���һ���ļ�:')
differ = file_compare(file1,file2)

if len(differ) == 0:
    print('�����ļ���ȫһ��')
else:
    print('�����ļ����С�%d������ͬ:' % len(differ))
    for each in differ:
        print('��%d�в�һ��' % each)




