def intersecao_de_lista(lista1,lista2):
    lista_intersecao=[]
    for elemento1 in lista1:
        if elemento1 in lista2:
            lista_intersecao.append(elemento1)
    return lista_intersecao