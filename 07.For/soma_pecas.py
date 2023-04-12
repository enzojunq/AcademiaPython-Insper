def soma_pecas(pecas):
    soma=0    
    for peca in pecas:
        soma+=peca[0]+peca[1]
    return soma
print(soma_pecas([[1,0],[2,3],[6,6]]))