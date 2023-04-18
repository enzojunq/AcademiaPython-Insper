# def verifica_ganhador(jogadores):
#     for indice,jogador in jogadores.items():
#         if len(jogador)==0:
#             return indice
#     return -1

def verifica_ganhador(jogadores):
    for jogador in jogadores:
        indice=jogadores[jogador]
        if len(indice)==0:
            return jogador
    return -1



jogadores={
    0: [[1,3],[0,1],[0,3],[0,4],[6,6],[0,6]],
    1: [[1,1],[1,2],[0,0],[1,4],[1,5]],
    2: [[3,6],[2,4],[3,4],[2,3]],
    3: []
}
print(verifica_ganhador(jogadores))