print('|--- ��ӭ����ͨѶ¼����---|')
print('|--- 1:��ѯ��ϵ������ ---| ')
print('|--- 2:�����µ���ϵ�� ---| ')
print('|--- 3:ɾ��������ϵ�� ---| ')
print('|--- 4:�˳�ͨѶ¼���� ---| ')

contacts = dict()
while 1:
    instr = int(input('\n��������ص�ָ�����:'))

    if instr == 1:
        name = input('��������ϵ������:')
        if name in contacts:
            print(name + ':' + contacts[name])
        else:
            print('���������������ͨѶ¼��!')
    if instr == 2:
        name = input('��������ϵ������:')
        if name in contacts:
            print('�������������ͨѶ¼���Ѵ���->>',end = '')
            print(name + ':' + contacts[name])
            if input('�Ƿ��޸��û�����(YES/NO):')=='YES':
                contacts[name] = input('�������û���ϵ�绰:')
        else:
            contacts[name]=input('�������û���ϵ�绰:')
    if instr == 3:
        name = input('��������ϵ������:')
        if name in contacts:
            del(contacts[name]) #Ҳ����ʹ��dict.pop()
        else:
            print('���������ϵ�˲����ڡ�')
    if instr == 4:
        break
print('|---��лʹ��ͨ��¼����---|')
