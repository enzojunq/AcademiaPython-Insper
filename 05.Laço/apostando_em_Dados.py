from random import randint
def apostando_em_dados(num_escolhido,aposta,num_rodadas):

    for i in range(num_rodadas):
        num_aleatorio = randint(1,6)
        if num_aleatorio == num_escolhido:
            aposta=aposta*(1+(1/3))
        else:
            aposta=aposta*(1-(1/6))
    return aposta
    
print(apostando_em_dados(5,180,3))
