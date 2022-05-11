#2022-04-20 最急降下法３ Gradient Descent

import random

A = 1
B = 5 
C = -3

alpha = 0.001 #ここを0.001にするなら
global a, b, c

def func_y_hat(x):                 
    return A * x * x + B * x + C   

def func_y(x):
    return a * x * x + b * x + c  

def func_error(y,y_hat):
    return 0.5 * (y - y_hat) * (y - y_hat)

def func_dd(x):
    d = func_y(x) - func_y_hat(x)
    return d * x * x, d * x, d     #a,b,cの偏微分まとめた

if __name__ == '__main__':

    i = 0
    j = 0
    a = random.random()
    b = random.random() 
    c = random.random()


for i in range(500):
    e_sum = 0

    for j in range(100):
        x = random.random() * 10 - 5    #ここの範囲を小さくする(-5から5)といける

        a -= alpha * func_dd(x)[0]
        b -= alpha * func_dd(x)[1]
        c -= alpha * func_dd(x)[2]

        e_sum += func_error(func_y(x), func_y_hat(x))

    e_ave = e_sum/100
    print(str(i)+' '+str(e_ave))

print('a = '+str(a)+' b = '+str(b)+' c = '+str(c))