from math import factorial
def calcula_euler(x,n):
    resultado=1+x
    '''while cont < n:
        resultado+=((x**cont)/factorial(cont))
        cont+=1'''
    for cont in range(2,n):
        resultado+=((x**cont)/factorial(cont))
    return resultado

print(calcula_euler(2,2))