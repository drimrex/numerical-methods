from math import *
def f(x):
    answer = x + sin(x) - 0.2*x
    return answer
n1 = 0
n2 = 2.6
count = 1
eps = 10**(-3)
print('0 = ',n2)
while abs(n2 - n1) > eps:
    n1 = n2
    n2 = round(f(n1), 3)
    print(count, '=', n2)
    count += 1
print('Ответ:',n2)