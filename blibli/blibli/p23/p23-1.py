# 课间联系:假设我们需要求出经历了20个月后,总共有多少对小兔崽子(迭代vs递归)
def rabbit_sum(n):
    if n < 1:
        print('输入有误!')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit_sum(n - 1) + rabbit_sum(n - 2)
    return rabbits_result


n = input('请输入第几个月:')
print(rabbit_sum(int(n)))
