def filtra_positivos(list):
    positivos=[]
    for i in range(len(list)):
        if list[i]>0:
            positivos.append(list[i])
    return positivos
lista=[-1,-2,3,4,5,6]
print(filtra_positivos(lista))