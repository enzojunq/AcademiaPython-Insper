def zera_negativos(numeros):
    for i in range(len(numeros)):
        if numeros[i]<0:
            numeros[i]=0
    return numeros
lista=[1,-1,2,-3,3,4]
print(zera_negativos(lista))