import math

def distancia_euclidiana(x1, x2, y1, y2):
    return math.sqrt((y1 - x1)**2 + (x2 - y2)**2)

def caminho_mais_curto(lista):
    distancias=[]
    for caminho in range(len(lista)):
        distancia=0
        for i in range(len(lista[caminho])-1):
            distancia+=distancia_euclidiana(lista[caminho][i][0], lista[caminho][i+1][0], lista[caminho][i][1], lista[caminho][i+1][1])
        distancias.append(distancia)
    index= distancias.index(min(distancias))
    return lista[index]

lista=[
    [[5, 2], [3, 7], [7, 3], [10, 4]],
    [[5, 2], [300, 1000], [10, 4]],
]
print(caminho_mais_curto(lista))