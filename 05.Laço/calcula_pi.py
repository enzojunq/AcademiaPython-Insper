def calcula_pi(n):
    i=1
    soma=0
    while i<=n:
        soma+=6/(i**2)
        i+=1
    pi=(soma)**(1/2)
    return pi