#coding:utf8
values = [1,1,2,3,5]
nums = set(values)
def checkit(num):
    if num in nums:
        return True
    else:
        return False

for i in filter(checkit, values):
    print(i, end='')