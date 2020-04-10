#coding:utf8
class C:
    @staticmethod #该修饰符表示static()是静态方法
    def static(arg1,arg2,arg3):
        print(arg1,arg2,arg3,arg1+arg2+arg3)

    def nostatic(self):
        print("I'm the f**king normal method!")
    #静态方法最大的优点是:不会绑定到实例对象上,换而言之就是节省开销
c1 = C()
c2 = C()
#静态方法只在内存中生成一个,节省开销
print(c1.static is C.static)
print(c1.nostatic is C.nostatic)
print(c1.static)
print(c2.static)
print(C.static)
print(c1.nostatic)
print(c2.nostatic)
print(C.nostatic)

print(c1.static(1,2,3))
print(C.static(1,2,3))