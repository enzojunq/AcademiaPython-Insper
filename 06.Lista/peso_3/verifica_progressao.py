def verifica_progressao(lista):
    AG=0
    PA=0
    PG=0
    if len(lista) < 3:
        return 'NA'
    
    if 0 in lista:
        return 'NA'
    
    for i in range(1,len(lista)-1):
        if lista[i]-lista[i-1]==lista[i+1]-lista[i] and lista[i]/lista[i-1]==lista[i+1]/lista[i]:
            AG+=1
        elif lista[i]-lista[i-1]==lista[i+1]-lista[i]:
            PA+=1
        elif lista[i-1]!=0 and lista[i]/lista[i-1]==lista[i+1]/lista[i]:
            PG+=1
        else:
            return 'NA'
    
    if AG==len(lista)-2:
        return 'AG'
    elif PA==len(lista)-2:
        return 'PA'
    else:
        return 'PG'

NA=[132,169,206,10]
PA=[1,2,3,4,5,6,7,8]
PG=[5,10,20,40,80,160]
AG=[1,1,1,1,1,1]

print(verifica_progressao(AG))
