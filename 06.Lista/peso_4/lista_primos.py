def eh_primo(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True


def lista_primos(n):
    i=1
    cont=0
    primos=[]
    while True:
        if eh_primo(i):
            primos.append(i)
            cont+=1
        if cont==n:
            break
        i+=1
    return primos

n=8
print(lista_primos(8))