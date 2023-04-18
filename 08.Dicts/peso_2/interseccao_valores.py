def interseccao_valores(dict1:dict,dict2:dict):
    lista_valores=[]
    for chave , valor in dict1.items():
        for chave2,valor2 in dict2.items():
            if valor==valor2:
                lista_valores.append(valor)
    return lista_valores