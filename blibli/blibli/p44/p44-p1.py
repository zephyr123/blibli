#coding:utf8
class Word:
    def __init__(self,string):
        self.str = string.split()[0]
        self.len = len(self.str)
    def __lt__(self, other):
        return self.len < other.len
    def __le__(self, other):
        return self.len <= other.len
    def __eq__(self, other):
        return self.len == other.len
    def __ne__(self, other):
        return self.len != other.len
    def __gt__(self, other):
        return self.len > other.len
    def __ge__(self, other):
        return self.len >= other.len

a = Word('Hello word!')
b = Word('hi word!')
print(a<b)