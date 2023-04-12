def adiciona_em_ordem(nome, distancia, lista):
    if len(lista) == 0:
        return [[nome, distancia]]

    for i in range(len(lista)):
        if distancia < lista[i][1]:
            lista.insert(i, [nome, distancia])
            break
    else:
        lista.append([nome, distancia])

    return lista


print(adiciona_em_ordem('libias', 14678, [
    ['libia', 3678],
    ['franca', 3998],
    ['egito', 5008],
    ['india', 9919],
    ['japao', 13836]
]))