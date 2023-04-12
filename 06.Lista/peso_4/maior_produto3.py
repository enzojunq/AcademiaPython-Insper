import itertools
def maior_produto3(lista):
    produto=[]
    for permutacao in itertools.permutations(lista, 3):
        produto.append(permutacao[0]*permutacao[1]*permutacao[2])

    return max(produto)
lista=[-1,-1,4,2,1]
print(maior_produto3(lista))