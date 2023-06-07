def inicia_jogo(jogadores, pecas):
    saida={'jogadores':{},'monte':[],'mesa':[]}
    pecas_ja_utilizadas=[]
    for i in range(jogadores):
        count=0
        saida['jogadores'][i]=[]
        for peca in pecas:
            if peca not in pecas_ja_utilizadas and count<7:
                saida['jogadores'][i].append(peca)
                pecas_ja_utilizadas.append(peca)
                count+=1

    for peca in pecas:
        if peca not in pecas_ja_utilizadas:
            saida['monte'].append(peca)
            
        
    return saida


jogadores = 2
pecas = [
	[1,3],[0,1],[4,6],[0,3],[0,4],[6,6],[0,6],
	[1,1],[1,2],[0,0],[1,4],[1,5],[1,6],[2,2],
	[3,6],[2,4],[2,5],[2,6],[3,3],[3,4],[2,3],
	[3,5],[4,4],[4,5],[0,2],[5,5],[5,6],[0,5]
]

print(inicia_jogo(jogadores, pecas))