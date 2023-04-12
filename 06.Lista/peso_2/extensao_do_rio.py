import math as m
def calcula_extensao(coord_x,coord_y):
    distancias=[]
    for i in range(len(coord_x)-1):
        distancias.append(m.sqrt(((coord_x[i+1]-coord_x[i])**2)+(coord_y[i+1]-coord_y[i])**2))
    return sum(distancias)
Coordenadas_x= [275, 290, 310, 390, 480]
Coordenadas_y= [75, 180, 120, 110, 150]
print(calcula_extensao(Coordenadas_x,Coordenadas_y))