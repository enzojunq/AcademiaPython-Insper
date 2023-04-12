def quantos_caminhoes(pesos):
    caminhoes=1
    soma=0
    for i in pesos:
        if soma+i<=2000:
            soma+=i
        else:
            caminhoes+=1
            soma=0
            soma+=i
    return caminhoes
pesos= [1000, 500, 400, 200]
print(quantos_caminhoes(pesos))