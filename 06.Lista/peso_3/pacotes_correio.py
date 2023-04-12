#Posição 0: número total de pacotes
#Posição 1: número daquele pacote (um inteiro, sequencial, crescente, que começa em um)
#Posição 2: tamanho do pacote (todos os pacotes devem ter um tamanho igual ao do primeiro)

def pacotes_correio(lista):
    if lista[0][0] != len(lista):
        return 'pacote perdido'
    for i, pacote in enumerate(lista):
        if pacote[1] != i+1:
            return 'ordem errada'
    for i in range(len(lista)):
        if lista[0][2] != lista[i][2]:
            return 'tamanho errado'
    
    else:
        return 'tudo certo'
        




remessa = [[4,1,20],[4,2,20],[4,3,20],[4,4,20]]
print(pacotes_correio(remessa))