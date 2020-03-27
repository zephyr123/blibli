#4.哎呀呀,现在的小孩太调皮了，邻居家的孩子淘气，把小甲鱼刚写好的代码画了个图案，
# 麻烦各位鱼油恢复下啊，另外这家伙画的神马吗？怎么那么眼熟啊？
name = input('请输入待查的用户名:')
sorce = [['迷途',85],['黑夜',80],['小布丁',65],['福禄娃娃',95],['怡静'],90]
isFind = False
for each in sorce:
    if name in each:
        print(name + '的分数是',each[1])
        isFind = True
        break
    # else:
if isFind == False:
    print('您查的用户不存在!')