def fatorial(n):
    resultado=1
    cont=1
    '''for i in range(n):
        resultado*=n
        n-=1'''
    
    while cont < n:
        resultado*=n
        n-=1
    return resultado
print(fatorial(5))
