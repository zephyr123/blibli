#coding:utf8
import time as t

class MyTimer:
    def __init__(self):
        self.prompt = '未开始计时!'
        self.lasted = 0.0
        self.begin = 0
        self.end = 0
        self.default_timer = t.perf_counter
    def __str__(self):
        return self.prompt
    __repr__ = __str__

    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = "总共运行了%0.2f秒" %result
        return prompt
    #开始计时
    def start(self):
        self.begin = self.default_timer()
        self.prompt = "提示:请先调用stop()停止计时"
        print("计时开始...")
    #停止计时
    def stop(self):
        if not self.begin:
            print("提示:请先调用start()进行计时")
        else:
            self.end = self.default_timer()
            self._calc()
            print("计时结束!")
    #内部方法,计算运行时间
    def _calc(self):
        self.lasted = self.end - self.begin
        self.prompt = "总共运行了%0.2f秒" % self.lasted

        #为下一轮计时初始化变量
        self.begin = 0
        self.end = 0
    #设置计时器(time.perf_counter()或time.process_time())
    def set_timer(self,timer):
        if timer == 'process_time':
            self.default_timer = t.process_time
        elif timer == 'perf_counter':
            self.default_timer = t.perf_counter
        else:
            print('输入无效,请输入perf_counter或process_time')

t1 = MyTimer()
t1.start()
t.sleep(3)
t1.stop()
print(t1)
t2 = MyTimer()
t2.set_timer('process_time')
t2.start()
t.sleep(5)
t2.stop()
print(t2)