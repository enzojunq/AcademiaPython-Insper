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


def primos_no_intervalo(a,b):
    primos = []
    for i in range(a,b+1):
        if eh_primo(i):
            primos.append(i)
    return primos

print(primos_no_intervalo(1,10))