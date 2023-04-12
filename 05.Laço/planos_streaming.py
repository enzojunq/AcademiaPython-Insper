novo=['the circle','mad men']
padrao=['stranger things','friends','the circle','mad men']
premium=['stranger things','friends','the circle','mad men','brasileirao','champions']

plano=input('Qual plano voce deseja? ').lower()

if plano == 'novo':
    while True:
        serie=input('Qual serie voce deseja assistir? ')
        if serie=='sair':
            print('Ok, tchau!')
            break
        elif serie in novo:
            print('Ok, reproduzindo!')
            print('Num oferecimento de DesSoft!')
        elif serie in padrao or serie in premium:
            print('Precisa comprar novo plano!')
        else:
            print('Serie inexistente!')   
elif plano == 'padrao':
    while True:
        serie=input('Qual serie voce deseja assistir? ')
        if serie=='sair':
            print('Ok, tchau!')
            break
        elif serie in padrao:
            print('Ok, reproduzindo!')
        elif serie in novo or serie in premium:
            print('Precisa comprar novo plano!')
        else:
            print('Serie inexistente!') 
elif plano == 'premium':
    while True:
        serie=input('Qual serie voce deseja assistir? ')
        if serie=='sair':
            print('Ok, tchau!')
            break
        elif serie in premium:
            print('Ok, reproduzindo!')
        elif serie in novo or serie in padrao:
            print('Precisa comprar novo plano!')
        else:
            print('Serie inexistente!') 
else:
    print('Plano invalido')