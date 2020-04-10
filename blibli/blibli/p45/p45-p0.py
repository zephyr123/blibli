#coding:utf8
import time  as t
class MyTimer():
    def __init__(self):
        self.unit = ['年','月','天','小时','分钟','秒']
        self.prompt = '未开始计时!'
        self.lasted = []
        self.new = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
        result = self._transferMax(result)
        for index in range(6):
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
    #开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示:请先调用stop()停止计时！"
        print("计时开始...")
    #停止计时
    def stop(self):
        if not self.begin:
            print("提示:请先调用start()进行计时!")
        else:
            self.end = t.localtime()
            self._calc()
            print('计时结束!')
    def _transferMax(self,res):
        res.reverse()
        for i in range(3):
            if res[i] > 60:
                res[i+1] += (res[i] // 60)
                res[i] = (res[i] % 60)
        if res[3] > 31:
            res[3] -= 31
            res[4] += 1
        if res[4]  > 12:
            res[4] -= 12
            res[5] += 1
        res.reverse()
        return res

    #时间转换为正数
    def _transferMin(self,data):
        data.reverse()
        for i in range(3):
            if data[i] < 0:
                data[i] += 60
                data[i+1] -= 1
        if data[3] < 0:
            data[3] += 31
            data[4] -= 1
        if data[4] < 0:
            data[4] += 12
            data[5] -= 1
        data.reverse()
        return data
    #内部方法,计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        print(self.begin, self.end);
        exit()
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
        self.lasted = self._transferMin(self.lasted)
        for index in range(6):
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]

        #为下一轮计时初始化变量
        self.begin = 0
        self.end = 0

t1 = MyTimer()
t1.start()
t.sleep(5)
t1.stop()
print(t1)

t2 = MyTimer()
t2.start()
t.sleep(6)
t2.stop()
print(t2)
print(t1 + t2)