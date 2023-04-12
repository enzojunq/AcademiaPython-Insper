sequencias = []
for i in range(1, 999):

    cont = 1
    while i != 1:
        if i % 2 == 0:
            i /= 2
            cont += 1
        elif i % 2 != 0:
            i = 3 * i + 1
            cont += 1
    sequencias.append(cont)
maximo = sequencias.index(max(sequencias)) + 1
print(maximo)