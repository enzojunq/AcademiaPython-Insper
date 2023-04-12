def soma_multiplos(x,y):
    soma=0
    if x>y:
        maior=x
    else:
        maior=y

    multiplo=maior*10
    
    for i in range(multiplo+1):
        if i%x==0:
            soma=soma+i
    for i in range(multiplo+1):
        if i%y==0 and i%x!=0:    
            soma=soma+i
    return soma


print(soma_multiplos(7,4))