def test(*params,exp):
    print('参数的长度是:',len(params),exp);
    print('第二个参数是:',params[1]);
test(1,'小甲鱼',3.14,5,6,7,exp=8)