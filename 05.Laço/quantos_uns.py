def quantos_uns(x):
    numero = str(x)
    posicao = 0
    cont = 0
    while posicao < len(numero):
        if numero[posicao] == '1':
            cont += 1
        posicao += 1
    return cont