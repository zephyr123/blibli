#coding:utf8
import time  as t
class MyTimer():
    def __init__(self):
        self.prompt = '未开始计时!'
        self.pro_prompt = ''
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt + self.pro_prompt

    __repr__ = __str__

    def __add__(self, other):
        prompt = "总共运行了"
        prompt += str(self.lasted + other.lasted) + '秒'
        return prompt

    def timing(self):
        self.start()
    #开始计时
    def start(self):
        self.begin = t.perf_counter()
        self.prompt = "提示:请先调用stop()停止计时！"
        print("计时开始...")
    #停止计时
    def stop(self):
        if not self.begin:
            print("提示:请先调用start()进行计时!")
        else:
            self.end = t.perf_counter()
            self.pro_end = t.process_time()
            self._calc()
            print('计时结束!')

    #内部方法,计算运行时间
    def _calc(self):
        self.lasted = self.end - self.begin
        self.prompt = "总共运行的精确时间为:"
        self.pro_prompt = "程序运行时间为:"
        self.prompt += str(self.lasted) + ' 秒'
        self.pro_prompt += str(self.pro_end) + ' 秒'
        #为下一轮计时初始化变量
        self.begin = 0
        self.end = 0

t1 = MyTimer()
print(t1)
t1.timing()
t.sleep(5)
t1.stop()
