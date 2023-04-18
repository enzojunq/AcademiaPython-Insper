def primeiras_ocorrencias(string):
    letras={}
    for letra in range(len(string)):
        if string[letra] not in letras:
            letras[string[letra]]=letra
    return letras


entrada='abracadabra'
print(primeiras_ocorrencias(entrada))