def verifica_jogo_da_velha(tabuleiro):
    for linha in tabuleiro:
        if linha[1]==linha[2]==linha[0]:
            return linha[0]
    for i in range(3):
        if tabuleiro[0][i]==tabuleiro[1][i]==tabuleiro[2][i]:
            return tabuleiro[0][i]
    if tabuleiro[0][0]==tabuleiro[1][1]==tabuleiro[2][2]:
        return tabuleiro[0][0]
    if tabuleiro[0][2]==tabuleiro[1][1]==tabuleiro[2][0]:
        return tabuleiro[0][2]
    return 'V'

tabuleiro = [['X', 'O', 'X'], ['O', 'O', 'O'], ['O', 'X', 'X']]
print(verifica_jogo_da_velha(tabuleiro))