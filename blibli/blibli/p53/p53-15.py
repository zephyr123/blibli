#coding:utf8
import copy
list1 = [1,2]
list2 = [3,4]
dict1 = {'1':list1,'2':list2}
dict2 = copy.deepcopy(dict1)

dict1['1'][0] = 5
result = dict1['1'][0] + dict2['1'][0]
print(result)