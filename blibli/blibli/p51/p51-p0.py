#该模块用于让python支持常量操作
class Const:
    def __setattr__(self, key, value):
        if name in self.__dict__:
            raise TypeError('常量无法改变')
        if not name.isupper():
            raise TypeError('常量名必须由大写字母组成!')
        self.__dict__[name] = value

import  sys
sys.modules[__name__] = Const()
