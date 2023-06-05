import math as m
def distancia_euclidiana(x1,x2,y1,y2):
    distancia=m.sqrt((x2-x1)**2+(y2-y1)**2)
    return distancia
def classifica(padroes,medida):
    menor=-1
    menor_peixe=[]
    for peixes, medidas in padroes.items():
        for tamanho in medidas:
            distancia=distancia_euclidiana(tamanho[0],medida[0],tamanho[1],medida[1])
            if menor ==-1:
                menor = distancia_euclidiana(tamanho[0],medida[0],tamanho[1],medida[1])
                menor_peixe.append(peixes)
            elif distancia <menor:
                menor = distancia
                menor_peixe.append(peixes)
    return menor_peixe[-1]



padroes = {
    'salmao': [[8, 6], [12, 5], [10, 4]],
    'robalo': [[9, 3], [8, 2], [7, 3]],
    'sardinha': [[1, 2], [2, 3], [2, 2]]
}

medida = [10,4]
print(classifica(padroes,medida))