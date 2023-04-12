def calcula_serie(a,b,n):
    soma = 0
    for i in range(n):
        soma += (1/(a**(i*b)))
    return soma
print(calcula_serie(2,1,1))