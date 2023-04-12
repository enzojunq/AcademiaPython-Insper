def classifica_trigo(lista):
    resultado=[]
    for trigo in lista:
        if trigo <= 2:
            resultado.append('T1')
        elif trigo <= 3:
            resultado.append('T2')
        elif trigo <= 7:
            resultado.append('T3')
        else:
            resultado.append('FT')
    return resultado