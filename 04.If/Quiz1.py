tamanho_bolo=input('Qual o tamanho do bolo? ')
tamanhos = ['XP','P','M','G','XG']
precos = [5,7,20,31,50]

orcamento = float(input("Qual o orçamento disponível?" ))

if tamanho_bolo in tamanhos:
    index=precos[tamanhos.index(tamanho_bolo)]
    if orcamento//index<=4:
        resto=orcamento%index
        if resto==0:
            print('sem acompanhamento')
        elif resto==1:
            print('1 brownie')
        elif resto%2==0:
            print(f'{int(resto//2)} cheesecake')
        else:
            print(f'{int(resto//2)} cheesecake')
            print('1 brownie')

    elif orcamento//index>4:
        resto=orcamento%index
        if resto==0:
            print('sem acompanhamento')
        elif resto==1:
            print('1 banoffee')
        elif resto%2==0:
            print(f'{int(resto//2)} cupcake')
        else:
            print(f'{int(resto//2)} cupcake')
            print('1 banoffee')
