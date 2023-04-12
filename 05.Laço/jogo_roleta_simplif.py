import random
dinheiro=100
while dinheiro>0:
    print(dinheiro)
    aposta=float(input('Quanto você quer apostar? '))
    if aposta==0:
        break
    aposta2=input('Você quer apostar em um número ou em uma paridade? ')
    if aposta2=='n':
        numero=int(input('Qual número você quer apostar? '))
        if numero==0:
            break
        numero2=random.randint(0,36)
        if numero==numero2:
            dinheiro+=35*aposta
        else:
            dinheiro-=aposta
    elif aposta2=='p':
        paridade=input('Você quer apostar em par ou ímpar? ')
        numero2=random.randint(0,36)
        if paridade=='p':
            if numero2%2==0:
                dinheiro+=aposta
            else:
                dinheiro-=aposta
        elif paridade=='i':
            if numero2%2==1:
                dinheiro+=aposta
            else:
                dinheiro-=aposta
