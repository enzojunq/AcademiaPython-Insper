def junta_listas(lista):
    lista_simples=[]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            lista_simples.append(lista[i][j])
    return lista_simples