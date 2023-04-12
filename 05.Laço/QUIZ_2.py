import math
##tamanho_bolo=input('Qual o tamanho do bolo? ')
##orcamento=float(input('Qual o orcamento disponível? '))

tamanho_bolo='G'
orcamento=135

if tamanho_bolo=='XP':
    if orcamento/5<=4:    
        if orcamento <=5:
            print('sem acompanhamento')
        elif orcamento>5:
            resto=math.floor(orcamento%5)
            if resto==0:
                print('sem acompanhamento')
            elif resto!=0 and math.floor(resto%2)==0:
                print(f'{math.floor(resto/2)} cheesecake')
            else:
                print(f'{math.floor(resto/2)} cheesecake')
                print('1 brownie')
    else:
        if orcamento <=5:
            print('sem acompanhamento')
        elif orcamento>5:
            resto=math.floor(orcamento%5)
            if resto==0:
                print('sem acompanhamento')
            elif resto!=0 and math.floor(resto%2)==0:
                print(f'{math.floor(resto/2)} cupcake')
            else:
                print(f'{math.floor(resto/2)} cupcake')
                print('1 banoffee')
elif tamanho_bolo=='P':
    if orcamento/7<=4:    
        if orcamento <=7:
            print('sem acompanhamento')
        elif orcamento>7:
            resto=math.floor(orcamento%7)
            if resto==0:
                print('sem acompanhamento')
            elif resto!=0 and math.floor(resto%2)==0:
                print(f'{math.floor(resto/2)} cheesecake')
            else:
                print(f'{math.floor(resto/2)} cheesecake')
                print('1 brownie')
    else:
        if orcamento <=7:
            print('sem acompanhamento')
        elif orcamento>7:
            resto=math.floor(orcamento%7)
            if resto==0:
                print('sem acompanhamento')
            elif resto!=0 and math.floor(resto%2)==0:
                print(f'{math.floor(resto/2)} cupcake')
            else:
                print(f'{math.floor(resto/2)} cupcake')
                print('1 banoffee')
elif tamanho_bolo=='M':
    if orcamento/20<=4:    
        if orcamento <=20:
            print('sem acompanhamento')
        elif orcamento>20:
            resto=math.floor(orcamento%20)
            if resto==0:
                print('sem acompanhamento')
            elif resto!=0 and math.floor(resto%2)==0:
                print(f'{math.floor(resto/2)} cheesecake')
            else:
                print(f'{math.floor(resto/2)} cheesecake')
                print('1 brownie')
    else:
        if orcamento <=20:
            print('sem acompanhamento')
        elif orcamento>20:
            resto=math.floor(orcamento%20)
            if resto==0:
                print('sem acompanhamento')
            elif resto!=0 and math.floor(resto%2)==0:
                print(f'{math.floor(resto/2)} cupcake')
            else:
                print(f'{math.floor(resto/2)} cupcake')
                print('1 banoffee')
elif tamanho_bolo=='G':
    if orcamento/31<=4:    
        if orcamento <=31:
            print('sem acompanhamento')
        elif orcamento>31:
            resto=orcamento%31
            if resto==0:
                print('sem acompanhamento')
            elif resto!=0 and math.floor(resto%2)==0:
                print(f'{math.floor(resto/2)} cheesecake')
            else:
                print(f'{math.floor(resto/2)} cheesecake')
                print('1 brownie')
    else:
        if orcamento<=31:
            print('sem acompanhamento')
        elif orcamento>31:
            resto=math.floor(orcamento%31)
            if resto==0:
                print('sem acompanhamento')
            elif resto!=0 and math.floor(resto%2)==0:
                print(f'{math.floor(resto/2)} cupcake')
            else:
                print(f'{math.floor(resto/2)} cupcake')
                print('1 banoffee')
elif tamanho_bolo=='XG':
    if orcamento/50<=4:    
        if orcamento <=50:
            print('sem acompanhamento')
        elif orcamento>50:
            resto=math.floor(orcamento%50)
            if resto==0:
                print('sem acompanhamento')
            elif resto!=0 and math.floor(resto%2)==0:
                print(f'{math.floor(resto/2)} cheesecake')
            else:
                print(f'{math.floor(resto/2)} cheesecake')
                print('1 brownie')
    else:
        if orcamento <=50:
            print('sem acompanhamento')
        elif orcamento>50:
            resto=math.floor(orcamento%50)
            if resto==0:
                print('sem acompanhamento')
            elif resto!=0 and math.floor(resto%2)==0:
                print(f'{math.floor(resto/2)} cupcake')
            else:
                print(f'{math.floor(resto/2)} cupcake')
                print('1 banoffee')
