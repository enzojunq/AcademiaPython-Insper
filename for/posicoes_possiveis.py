def posicoes_possiveis(mesa,pecas):
    mesa_num=[]
    posicoes=[]

    if len(mesa) == 0:
        for i in range(len(pecas)):
            mesa_num.append(i)
        return mesa_num
    numero_1=mesa[0][0]
    posicoes.append(numero_1)
    tamanho=len(mesa)-1
 
    posicoes.append(mesa[tamanho][1])




    for i in range(len(pecas)):
        if pecas[i][0] in posicoes or pecas[i][1] in posicoes :
            mesa_num.append(i)

    return mesa_num
    

mesa=[[0, 2], [2, 1], [1, 6], [6, 5], [5, 3]]
jogador=[[1, 3], [0, 1], [0, 4], [6, 6], [0, 6]]
print(posicoes_possiveis(mesa,jogador))