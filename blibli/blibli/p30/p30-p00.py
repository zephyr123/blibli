
def file_write(file_name):
    f = open(file_name,'w')
    print('���������ݡ���������\':w\'�������˳�:')

    while True:
        write_some = input()
        if write_some != ':w':
            f.write('%s\n'% write_some)
        else:
            break
    f.close()

file_name = input('�������ļ���:')
file_write(file_name)