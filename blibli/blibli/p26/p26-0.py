print('|--- 欢迎进入通讯录程序---|')
print('|--- 1:查询联系人资料 ---| ')
print('|--- 2:插入新的联系人 ---| ')
print('|--- 3:删除已有联系人 ---| ')
print('|--- 4:退出通讯录程序 ---| ')

addressBook = {}
while True:
    number = int(input('\n请输入相关指令代码:'))
    if number == 2:
        name1=input('请输入联系人姓名:')
        if name1 in addressBook:
            print('您输入的姓名在通讯录中已存在-->>'+ name1 + ':' + addressBook[name1])
            temp = input('是否修改用户资料 (YES/NO):')
            if temp == 'YES':
                phone=input('请输入用户联系电话:')
                addressBook[name1]=phone
        else:
            phone = input('请输入联系人电话:')
        addressBook[name1] = phone
    elif number == 1:
        name = input('\n请输入联系人姓名:')
        if name in addressBook:
            print(name + ':' + addressBook[name])
    elif number == 4:
        print('|---感谢使用通讯录程序!---|')
        break






