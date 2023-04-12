import numpy as np

def produz_um_dois_insper(num_i, num_f, multiplo):
    lista = list(range(num_i, num_f+1))
    #print(lista)
    for i, valor in enumerate(lista):
        #print(valor, i)
        if (valor % multiplo) == 0:
            lista[i] = 'Insper' # type: ignore
    return lista

print(produz_um_dois_insper(2, 13, 3))
