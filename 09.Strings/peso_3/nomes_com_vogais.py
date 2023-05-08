lista_vogais='AEIOU'
def nomes_com_vogais(lista_nomes):
    vogais=0
    consoantes=0
    for nome in lista_nomes:
        if nome[0] in lista_vogais:
            vogais+=1
        else:
            consoantes+=1
    return [vogais,consoantes]


nomes=["André", "Carlos", "João", "Otavio", "Thiago"]
print(nomes_com_vogais(nomes))