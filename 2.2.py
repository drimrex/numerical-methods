from math import *
def f(x):
    num = 2**x - 2*cos(x)
    return num
eps = 1
a = 0.5
b = 1
while eps > 0.001:
    c = (a + b)/2
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
        eps = (b - a)/2
Answer = (a + b)/2
print(Answer)