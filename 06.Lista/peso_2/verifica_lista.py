def verifica_lista(list):
    pares=[]
    impares=[]
    for i in range(len(list)):
        if list[i]%2==0:
            pares.append(list[i])
        else:
            impares.append(list[i])
    if len(pares)>0 and len(impares)>0:
        return 'misturado'
    elif len(pares)==0 and len(impares)>0:
        return 'ímpar'
    elif len(pares)>0 and len(impares)==0:
        return 'par'
    else:
        return 'misturado'