def conta_ocorrencias(lista):
    palavras={}
    for palavra in lista:
        if palavra not in palavras:
            palavras[palavra]=1
        else:
            palavras[palavra]+=1
    return palavras

entrada=['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']
print(conta_ocorrencias(entrada))