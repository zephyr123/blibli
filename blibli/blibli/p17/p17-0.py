#猜想一下 min()这个BIF的实现过程。
def min(x):
    least = x[0]
    for each in x:
        if least > each:
            least = each


    return least

print(min('1234567890'))