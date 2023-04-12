def encontra_maximo(lista):
    maximo=[]
    maximo_abs=[]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            maximo.append(lista[i][j])
    for i in range(len(maximo)):
        maximo_abs.append(abs(maximo[i]))

    return max(maximo_abs)

lista = [[1, 2, -30], [4, 5, 6], [7, 8, 9]]
print(encontra_maximo(lista))