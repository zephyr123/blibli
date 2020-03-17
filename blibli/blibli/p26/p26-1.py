dict1 = {}
dict1 = dict1.fromkeys(range(32),'赞')
print(dict1)

for eachKey in dict1.keys():
    print(eachKey)

for eachValue in dict1.values():
    print(eachValue)

for eachItem in dict1.items():
    print(eachItem)