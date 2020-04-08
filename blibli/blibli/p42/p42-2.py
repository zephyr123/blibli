#coding:utf8
class Capstr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls,string)


a = Capstr("I love FishC.com")
print(a)
