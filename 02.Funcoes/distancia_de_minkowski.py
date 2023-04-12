import math

def distancia(x1,y1,x2,y2,p):
    abs1=abs(x1-x2)**p
    abs2=abs(y1-y2)**p
    d = (abs1+abs2)**(1/p)

    return d 