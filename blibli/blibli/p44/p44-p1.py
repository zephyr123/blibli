#coding:utf8
class Word(str):
    def __lt__(self, other):
        if len(str.self) < len(strother):
            return self < other

a = Word('abc')
b = Word('abcd')
print(a<b)