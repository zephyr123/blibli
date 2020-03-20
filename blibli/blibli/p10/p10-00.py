count=3
password='FishC123'
while count:
    passwd=input('请输入你的密码:')
    if passwd == password:
        print('密码输入正确！')
        break
    elif '*' in passwd:
        print('密码中不能有"*"号，您还有',count ,'次机会',end='')
        continue
    else:
        print('输入错误,您还有',count-1,'次输入机会.',end='')
        count-=1
