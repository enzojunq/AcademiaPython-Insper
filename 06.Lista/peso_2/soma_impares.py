def soma_impares(numeros):
    impares=[]
    for i in range(len(numeros)):
        if numeros[i]%2!=0:
            impares.append(numeros[i])
    return sum(impares)