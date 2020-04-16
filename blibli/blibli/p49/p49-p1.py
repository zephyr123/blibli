#coding:utf8
import time
class LeapYear:
    def __init__(self):
        self.year = time.localtime()[0]
        self.year_list = []
    def __iter__(self):
        return self
    def __next__(self):
        if (self.year %4 == 0 and self.year %100 !=0) or (self.year%400 == 0):
            self.year_list.append(self.year)
        self.year -= 1
        print(self.year_list)
        return self.year_list
leapYears = LeapYear()
print(leapYears)

for i in leapYears:
    if i >= 2000:
        print(i)
    else:
        break


