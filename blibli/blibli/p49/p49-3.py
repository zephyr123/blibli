#coding:utf8
string = 'FishC'
it = iter(string)
while True:
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)

