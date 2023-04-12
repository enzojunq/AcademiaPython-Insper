def eh_respiravel(listas):
    cont=0
    cont2=0
    for lista in listas:
        cont+=lista.count('O')
        cont2+=len(lista)
    if cont/cont2>=0.20:
        return True
    else:
        return False



listas = [
    ['O', 'N', 'O', 'Rn'],
    ['Ar', 'O', 'He', 'N'],
    ['Uuo', 'O', 'O', 'O'],
    ['O', 'O', 'N', 'O']
]
lista2=[['N', 'N', 'N', 'Xe', 'O', 'N', 'N', 'O', 'N', 'N'], ['N', 'Xe', 'N', 'He', 'N', 'O', 'O', 'N', 'N', 'N'], ['Kr', 'N', 'N', 'Ar', 'N', 'O', 'Xe', 'O', 'N', 'O'], ['Ne', 'N', 'N', 'Xe', 'Kr', 'N', 'Kr', 'Rn', 'O', 'Ar'], ['Rn', 'Xe', 'Ne', 'Xe', 'N', 'N', 'N', 'N', 'N', 'O'], ['N', 'N', 'O', 'O', 'Xe', 'N', 'N', 'Ar', 'N', 'O']]

print(eh_respiravel(lista2))