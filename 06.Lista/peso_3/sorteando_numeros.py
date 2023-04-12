import random
def distribuir(n,lista):
    i=0
    resultado=[]
    while i < n:
        aleatorio=random.randint(0,len(lista)-1)
        numero = lista[aleatorio]
        if numero not in resultado:
            resultado.append(numero)
            i+=1
    return resultado

print(distribuir(2,[1,2,2,2,2,2]))