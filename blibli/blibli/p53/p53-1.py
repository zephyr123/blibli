#coding:utf8
country_counter = {}
def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1

addone('China')
addone('Japan')
addone('China')
addone('American')
print(len(country_counter))