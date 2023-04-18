def contagem_caracteres(string):
    letras={}
    for letra in string:
        if letra not in letras:
            letras[letra]=0
            letras[letra]+=1
        else:
            letras[letra]+=1
    return letras

entrada='abracadabra'
print(contagem_caracteres(entrada))