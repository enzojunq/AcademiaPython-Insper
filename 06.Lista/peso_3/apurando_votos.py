def apurando_votos(candidatos, votos):
    votos_invalidos = 0
    contador = {}

    for voto in votos:
        if voto not in candidatos:
            votos_invalidos += 1
        elif voto in contador:
            contador[voto] += 1
        else:
            contador[voto] = 1
    print(contador)
    if max(contador.values()) <= votos_invalidos:
        return 'CANCELADA'
    else:
        # Encontrando a chave com o valor máximo no dicionário
        vencedor = max(contador, key=contador.get)
        return vencedor

candidatos = ['Maria', 'Joana', 'Marcos', 'Paulo', 'Joaquim']
votos = ['Maria', 'teste', 'Joana', 'Marcos', 'Paulo', 'Joaquim', 'Marcos', 'Paulo', 'Joaquim']

print(apurando_votos(candidatos, votos))
