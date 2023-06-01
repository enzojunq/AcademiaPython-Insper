def conta_bigramas(frase):
    bigramas={}

    for i in range(len(frase)-1):
        if frase[i:i+2] not in bigramas:
            bigramas[frase[i:i+2]]=1
        else:
            bigramas[frase[i:i+2]]+=1

    return bigramas

frase = 'banana nanica'
print(conta_bigramas(frase))
    