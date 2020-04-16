#coding:utf8
import time as t
class Record:
    def __init__(self,initval=None,name=None):
        self.val = initval
        self.name = name
        self.filename = 'F:\\python_work\\blibli\\blibli\\p47\\record.txt'
    def __get__(self, instance, owner):
        with open(self.filename,'a',encoding='utf8')  as f:
            f.write('%s变量于北京时间%s被读取,%s = %s\n'% (self.name,t.ctime(),self.name,self.val))
        return self.val
    def __set__(self, instance, value):
        with open(self.filename,'a',encoding='utf8') as f:
            f.write('%s变量于北京时间%s被修改,%s = %s \n' % (self.name,t.ctime(),self.name,str(value)))
        self.val = value


class Test:
    x = Record(10,'x')
    y = Record(8.8,'y')

test = Test()
print(test.x)
print(test.y)
