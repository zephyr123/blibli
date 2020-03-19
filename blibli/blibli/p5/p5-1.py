temp = input('请输入一个年份:')
while not temp.isdigit():
    temp = input('请输入一个数字年份:')
year = int(temp)
if (year % 4 == 0 )  and (year %100 !=0):
    print(temp + '是闰年')
elif (year % 400 == 0):
    print(temp + '是闰年')
else:
    print(temp + '不是闰年')