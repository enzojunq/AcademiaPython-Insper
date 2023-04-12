def calcula_escola(lista):
    minimo=[]
    soma=0
    for i in lista:
        minimo.append(min(i))
        print(minimo)

    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if minimo[i] == lista[i][j]:
                del(lista[i][j])
                print(lista[i])
                break

    for i in lista:
        soma+=sum(i)
    return soma


tom_maior = [[9.9, 9.9, 10, 9.9], [10, 9.9, 9.8, 10], [10, 10, 10, 10], [10, 10, 10, 10], [10, 9.9, 9.9, 10], [9.9, 10, 10, 10], [10, 10, 9.9, 9.9], [0.0, 9.9, 10, 9.9], [10, 9.8, 10, 10]]
print(calcula_escola(tom_maior))