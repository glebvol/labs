import math as m
def F(x,y):
    return m.sin(x+1)-y-1.2
def G(x,y):
    return 2*x+m.cos(y)-2
def F1x(x,y):
    return m.cos(x+1)
def G1x(x,y):
    return 2
def F1y(x,y):
    return -1
def G1y(x,y):
    return -m.sin(y)
eps=0.0001
xn=-10
yn=-10
h=(-G(xn,yn)*F1x(xn,yn)/G1x(xn,yn)+F(xn,yn))/(G1y(xn,yn)*F1x(xn,yn)/G1x(xn,yn)-F1y(xn,yn))
g=(-F(xn,yn)-F1y(xn,yn)*h)/F1x(xn,yn)
xn1=xn+g
yn1=yn+h
while abs(xn1-xn)>eps or abs(yn1-yn)>eps:
    xn=xn1 
    yn=yn1
    h=(-G(xn,yn)*F1x(xn,yn)/G1x(xn,yn)+F(xn,yn))/(G1y(xn,yn)*F1x(xn,yn)/G1x(xn,yn)-F1y(xn,yn))
    g=(-F(xn,yn)-F1y(xn,yn)*h)/F1x(xn,yn)
    xn1=xn+g
    yn1=yn+h    
print('решение системы:')
print('sin(x+1)-y=1,2;')
print('2x+cos(y)=2;')
print(' x = %.5f y = %.5f ' %(xn1,yn1))