def discounts(price, rate):
    final_price = price * rate  # 这里是局部变量
    old_price = 88  # 这里修改全局变量
    print('修改后old_price的值1是:', old_price)  # 打印的是局部变量的值
    return final_price


old_price = float(input('请输入原价:'))
rate = float(input('请输入折扣率:'))
new_price = discounts(old_price, rate)
print('修改后old_price的值2是:', old_price)  # 这里是全局变量的值
# print('折扣后价格是:', new_price)
# print('这里试图打印局部变量final_price的值:',final_price)
