def monta_dicionario(lista1,lista2):
    dicionario={}
    for i in range(len(lista1)):
        dicionario[lista1[i]]=lista2[i]
    
    return dicionario
lista1=['A','B']
lista2=[1,2]

print(monta_dicionario(lista1,lista2))
