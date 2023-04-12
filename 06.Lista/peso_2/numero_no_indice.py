def numero_no_indice(list):
    same=[]
    for i in range(len(list)):
        if list[i]==i:
            same.append(i)
    return same