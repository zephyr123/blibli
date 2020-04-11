#coding:utf8
class Demo:
    def __getattr__(self, name):
        self.name = 'FishC'
        return self.name

demo = Demo()
print(demo.x)
demo.x = 'X-man'
print(demo.x)
