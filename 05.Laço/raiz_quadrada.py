def raiz_quadrada(x):
    i=1
    cont=0
    resultado=x
    if x==0:
        return x
    elif x==1:
        return x 
    else:
        while i < x:
            resultado=resultado-i
            i=i+2
            cont=cont+1
            if resultado==0:
                return cont
    
        
print(raiz_quadrada(0))

'''def raiz_quadrada(n):
    c = 1
    soma = n
    raiz = 0
    while soma > 0:
        soma -= c
        c += 2
        raiz += 1
    return raiz
    

print(raiz_quadrada(63))'''