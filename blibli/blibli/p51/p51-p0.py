#��ģ��������python֧�ֳ�������
class Const:
    def __setattr__(self, key, value):
        if name in self.__dict__:
            raise TypeError('�����޷��ı�')
        if not name.isupper():
            raise TypeError('�����������ɴ�д��ĸ���!')
        self.__dict__[name] = value

import  sys
sys.modules[__name__] = Const()
