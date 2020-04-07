#-*- coding:utf8 -*-
class C:
    count = 0

a = C()
b = C()
c = C()
print(a.count)
print(b.count)
print(c.count)
c.count += 10
print(c.count)
print(a.count)
C.count += 100
print(c.count)
print(a.count)
print(b.count)
