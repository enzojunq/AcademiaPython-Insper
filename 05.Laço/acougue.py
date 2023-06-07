import math

carnes = {'patinho': {'tipo': 'bovino', 'preco': 40},'acem': {'tipo': 'bovino', 'preco': 34},'peito': {'tipo': 'frango','preco': 24}, 'sobrecoxa': {'tipo': 'frango', 'preco': 13}, 'bisteca': {'tipo': 'suíno', 'preco': 28}}
tipos = {'bovino': {'peso':0,'valor':0} , 'frango': {'peso':0,'valor':0}, 'suíno': {'peso':0,'valor':0}}

carne = input("Qual carne você deseja comprar? ")
total = 0
valor_bandeja = 0

if carne == '':
    print("O total da sua compra foi {:.2f}".format(total))
    exit()

while carne != 'pagar':

    if carne not in carnes:
        print("Carne nao reconhecida - tente novamente.")
    else:
        peso = float(input("Qual o peso da carne? "))
        tipos[carnes[carne]['tipo']]['peso'] += peso

        bandeja = input("Você deseja bandeja? ")
        if bandeja == 's':
            if peso < 1:
                valor_bandeja += 0
            else:
                valor_bandeja += 0.5*math.floor(peso)
        

        tipos[carnes[carne]['tipo']]['valor'] += peso*carnes[carne]['preco']






    carne = input("Qual carne você deseja comprar? ")


if tipos['bovino']['peso'] >= 3 and tipos['bovino']['peso'] < 5:
    tipos['bovino']['valor'] = tipos['bovino']['valor'] - 0.05*tipos['bovino']['valor']
elif tipos['bovino']['peso'] >= 5:
    tipos['bovino']['valor'] = tipos['bovino']['valor'] - 0.07*tipos['bovino']['valor']

for tipo in tipos:
    total += tipos[tipo]['valor']

total += valor_bandeja

if tipos['bovino']['peso'] > 0 and tipos['frango']['peso'] > 0 and tipos['suíno']['peso'] > 0:
    total = total - 0.1*total




print("O total da sua compra foi {:.2f}".format(total))