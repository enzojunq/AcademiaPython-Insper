def verifica_progressao(lista):
    if len(lista) < 3:
        return 'NA'
    
    if 0 in lista:
        return 'NA'
    
    q = lista[1] - lista[0]
    r = lista[1] / lista [0]

    valor = 'NA'

    for i in range(2, len(lista)):
        if lista[i] - lista[i-1] != q:
            valor = 'NA'
            break
        else:
            valor = 'PA'
    
    for i in range(2, len(lista)):
        if lista[i] / lista[i-1] != r:
            valor = 'NA'
            break
        else:
            valor = 'PG'
    
    for i in range(2, len(lista)):
        if (lista[i] - lista[i-1]) != (lista[i-1] - lista[i-2]):
            valor = 'NA'
            break
        else:
            valor = 'AG'
    
    return valor
    
    