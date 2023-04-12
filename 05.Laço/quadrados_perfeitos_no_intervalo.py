def quadrados_no_intervalo(a,b):
    i = a
    cont=0
    while i <= b:
        if i**0.5 == int(i**0.5):
            cont+=1
        i = i + 1
    return cont
print(quadrados_no_intervalo(1,5))