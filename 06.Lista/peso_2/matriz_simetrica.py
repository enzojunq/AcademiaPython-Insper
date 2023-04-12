def eh_simetrica(matriz):
    cont=0
    contador_total=0
    if len(matriz[0]) != len(matriz):
        return False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==matriz[j][i]:
                cont+=1
            contador_total+=1
    if cont == contador_total:
        return True
    else: 
        return False

T=[[1, 4, 6], [4, 7, 8], [6, 8, 9]]
F=[[50, 52, 55], [55, 56, 57], [57, 58, 59]]
print(eh_simetrica(F))