#coding:utf8
BaseAlias = BaseClass #为基类取别名

class Derived(BaseAlias):
    def meth(self):
        BaseAlias.meth(self) #通过别名访问基类
        ...