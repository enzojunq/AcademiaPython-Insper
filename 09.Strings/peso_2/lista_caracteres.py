def lista_caracteres(palavra):
    lista=[]
    for i in range(len(palavra)):
        if palavra[i] not in lista:
            lista+=palavra[i]
    return lista