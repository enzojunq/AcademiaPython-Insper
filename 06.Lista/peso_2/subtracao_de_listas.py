def subtracao_de_listas(lista1,lista2):
    for i in range(len(lista1)-1):
        for j in range(len(lista2)-1):
            if lista1[i]==lista2[j]:
                del lista1[i]
    return lista1

lista1 = [2, 7, 3.1, 'banana']
lista2 = [2, 'banana', 'carro']
print(subtracao_de_listas(lista1,lista2))