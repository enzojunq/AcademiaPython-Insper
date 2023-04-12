def estritamente_crescente(lista):

    if len(lista)==0:
        return []
    
    lista2=[lista[0]]

    for i in range(len(lista)): 
        maior=max(lista2)
        if lista[i]>maior:
            lista2.append(lista[i])
    return lista2

print(estritamente_crescente([1,3,2,3,4,6,5]))