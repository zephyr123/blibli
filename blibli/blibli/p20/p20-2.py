count = 5


def MyFun():
    global count  # 声明为count全局变量
    count = 10
    print(count)


MyFun()
print(count)
