def promocao_viagens(destinos):
    valores_promocao=[]
    destinos_promocao={}
    for destino, valor in destinos.items():
        if valor[0]==1:
            valor[1]*=0.9
            valor1=valor[1]
            valores_promocao.append(valor1)
        elif valor[0]==2:
            valor[1]*=0.8
            valor2=valor[1]
            valores_promocao.append(valor2)
        elif valor[0]==3:
            valor[1]*=0.7
            valor3=valor[1]
            valores_promocao.append(valor3)
        elif valor[0]==4:
            valor[1]*=0.6
            valor4=valor[1]
            valores_promocao.append(valor4)
        elif valor[0]==5:
            valor[1]*=0.5
            valor5=valor[1]
            valores_promocao.append(valor5)
    i=0
    for destino in destinos:
        destinos_promocao[destino]=valores_promocao[i]
        i+=1
        
    return destinos_promocao





destinos = {
    "Miami" : [1, 1000],
    "Ilhas Sandwich do Sul" : [4, 5000],
    "Barcelona" : [2, 2000],
    "Antártica" : [5, 200],
    "Buenos Aires" : [3, 500]
}
print(promocao_viagens(destinos))