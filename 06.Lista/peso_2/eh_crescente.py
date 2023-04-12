def eh_crescente(list):
    crescente=[]
    for i in range(len(list)-1):
        if list[i]<list[i+1]:
            crescente.append(list[i])
    if len(list)==1 or len(list)==0:
        return True
    elif len(crescente)==len(list)-1:
        return True
    else:
        return False