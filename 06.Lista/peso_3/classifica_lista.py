def classifica_lista(lista):
    cresc=0
    decresc=0

    if len(lista)<2:
        return 'nenhum'
    for i in range(1,len(lista)):
        if lista[i]>lista[i-1]:
            cresc+=1
        elif lista[i]<lista[i-1]:
            decresc+=1
    if cresc==len(lista)-1:
        return 'crescente'
    elif decresc==len(lista)-1:
        return 'decrescente'
    else:
        return 'nenhum'
        