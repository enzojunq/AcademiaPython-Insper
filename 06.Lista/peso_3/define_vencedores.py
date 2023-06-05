def define_vencedores(sorteados,cartelas):

    pontuacao={}
    resultado=[]
    for numero in sorteados:
        for jogador,lista in cartelas.items():
            for numero_sorteado in lista:
                if numero_sorteado == numero:
                    if jogador not in pontuacao:
                        pontuacao[jogador]=1
                    else:
                        pontuacao[jogador]+=1

    if pontuacao == {}:
        for nome in cartelas:
            resultado.append(nome)
        return resultado
    else:
        maximo=max(pontuacao.values())
        for nome,pontos in pontuacao.items():
            if pontos == maximo:
                resultado.append(nome)

        return resultado
    
sorteados = [21, 25, 26, 27, 29, 112, 214, 215, 216, 219]

cartelas = {
    'joao': [4, 10, 11, 17, 19],
    'maria': [1, 4, 5, 6, 11]
}

print(define_vencedores(sorteados,cartelas))