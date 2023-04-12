def lista_em_zigue_zague(lista):
    if len(lista) < 2:
        return True
    if lista[1]>lista[0]:
        for i in range(1,len(lista)):
            if i%2 == 0:
                if lista[i]>lista[i-1]:
                    return False
            else:
                if lista[i]<lista[i-1]:
                    return False
    elif lista[1]<lista[0]:
        for i in range(1,len(lista)):
            if i%2 == 0:
                if lista[i]<lista[i-1]:
                    return False
            else:
                if lista[i]>lista[i-1]:
                    return False
    else:
        return False        
    return True
