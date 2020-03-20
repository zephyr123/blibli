#2.三色球问题
#有红、黄、绿三种颜色的球，其中红球3个，黄球3个，绿球6个。
# 先将这12个球混合放在一个盒子中，从中任意摸出8个球，编程计算摸出球的各种颜色搭配。
print('red\tyellow\tbule')
for red in range(0,4):
    for yellow in range(0,4):
        for green in range(2,7):
            if red + yellow + green ==8:
                #注意,下边不是字符串拼接,因此不用"+"
                print(red,'\t',yellow,'\t',green)
#range(2,7)是产生[2,3,4,5,6]5个数，绿色不能是1个，因为红色和黄色一共才6个
