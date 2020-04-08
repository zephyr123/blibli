#coding:utf8
class C2F(float):
    def __new__(cls,x=0.0):
        return float.__new__(cls,x*1.8 + 32)

print(C2F(10.0))