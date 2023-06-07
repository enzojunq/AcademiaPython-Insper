
def eh_primo(x):
    cont=2
    if(x<=1):
        return False   
    else:
        while (cont<x):
            if x%cont==0:
                return False
            cont+=1
        else:
            return True


def verifica_primos(lista):
    dict_numeros={}
    for numero in lista:
        if numero not in dict_numeros:
            dict_numeros[numero]=eh_primo(numero)
        

    return dict_numeros

lista = [1,2,3,4,5,6,7,8,9,10]
print(verifica_primos(lista))