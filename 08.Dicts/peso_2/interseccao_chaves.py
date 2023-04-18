def interseccao_chaves(dict1:dict,dict2:dict):
    lista=[]
    for chave1 in dict1:
        for chave2 in dict2:
            if chave2 == chave1:
                lista.append(chave2)
    return lista


dict1= {'A': 1, 'B': 2, 'C': 3, 'D': 4}
dict2= {'A': 5, 'B': 6, 'C': 7, 'E': 8}
print(interseccao_chaves(dict1,dict2))