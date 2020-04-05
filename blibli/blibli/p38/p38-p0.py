#-*- coding:utf8 -*-
class Ticket:
    def __init__(self):
        self.price = 100

    def adult_price(self,adult_number):
        return self.price * int(adult_number)

    def child_price(self,child_number):
        return ((self.price /2) * int(child_number))

    def sum_price(self,week,adult_number,child_number):
        if week in ['1','2','3','4','5']:
            print('总价是:' + str(self.adult_price(adult_number) + self.child_price(child_number)))
        if week in ['6','7']:
            print('总价是:' + str((self.adult_price(adult_number) + self.child_price(child_number)) * 1.2 ))

adult_number = input('请输入成人数量:')
child_number = input('请输入小孩的数量:')
week = input('请输入周几?')
jiage = Ticket()
jiage.sum_price(week,adult_number,child_number)
