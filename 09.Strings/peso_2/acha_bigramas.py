def acha_bigramas(palavra):
    bigramas=[]
    for i in range(len(palavra)-1):
        if palavra[i]+palavra[i+1] not in bigramas:
            bigramas.append(palavra[i]+palavra[i+1])
    return bigramas

palavra='babador'
print(acha_bigramas(palavra))