import math

def distancia_euclidiana(x1, x2, y1, y2):
    return math.sqrt((y1 - x1)**2 + (x2 - y2)**2)

def entregador_mais_proximo(restaurante, entregadores):
    distancias=[]
    for entregador in entregadores:
        #print(entregador)
        distancia=distancia_euclidiana(restaurante[0],entregador[0],restaurante[1],entregador[1])
        #print(distancia)
        distancias.append(distancia)
    return distancias.index(min(distancias))


print(entregador_mais_proximo([15, 20],[
    [28, 4],
    [63, 87],
    [192, 643],
    [16, 19],
    [523, 32],
]))