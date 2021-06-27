import math as m
def F(x):
    return x-m.sin(x)-0.25

def F1(x):
    return 1-m.cos(x)
eps=0.0001
x0=0
xn=F(x0)
xn1=xn-F(xn)/F1(xn)
while abs(xn1-xn)>eps:
    xn=xn1 
    xn1=xn-F(xn)/F1(xn)
print('решение x-sin(x)=0,25:')
print(' x = %.5f  ' %(xn1))