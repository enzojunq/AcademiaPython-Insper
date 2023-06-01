def conta_ocorrencias(lista):
    palavras={}
    for palavra in lista:
        if palavra not in palavras:
            palavras[palavra]=1
        else:
            palavras[palavra]+=1
    return palavras

def mais_frequente(lista):
    palavras=conta_ocorrencias(lista)
    return max(palavras, key=palavras.get)