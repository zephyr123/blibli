def MyFirstFunction(name):
    '函数的定义过程中的name是叫形式参数'
    #因为它只是一个形式,表示占据一个参数位置
    print('传递进来的'+name+'叫做实参,因为Ta是具体的参数值')
# MyFirstFunction('小甲鱼')
print(MyFirstFunction.__doc__)