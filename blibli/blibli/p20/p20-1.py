count = 5


def MyFun():
    count = 10  # 全局变量会被局部变量所屏蔽，此处默认是局部变量
    print(10)


MyFun()
print(count)
