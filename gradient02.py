import random

alpha = 0.001
global a, b

#c=random.random() * 0.0001         乱数

def func_y_hat(x):
    return 5 * x - 3 + (2 * random.random() - 1.0)

def func_y(x):
    return a*x+b

def func_error(y,y_hat):
    return 0.5 * (y - y_hat) * (y - y_hat)

def func_da(x):
    y = func_y(x)
    y_hat = func_y_hat(x)
    return (y - y_hat) * x

def func_db(x):
    y = func_y(x)
    y_hat = func_y_hat(x)
    return (y - y_hat) * 1

if __name__ == '__main__':

    i = 0;  j = 0
    a = random.random(); 
    b = random.random()

for i in range(500):
    e_sum = 0

    for j in range(100):
        x = random.random() * 100 - 50
        a -= alpha * func_da(x)
        b -= alpha * func_db(x)
        e_sum += func_error(func_y(x), func_y_hat(x))

    e_ave = e_sum/100
    print(str(i)+' '+str(e_ave))

print('a = '+str(a)+'   b = '+str(b))