def inverte_dicionario(nomes):
    new_dict={}
    for nome,idade in nomes.items():
        if idade not in new_dict:
            new_dict[idade]=[nome]
        else:
            new_dict[idade].append(nome)
    #ordena o dict por idade
    new_dict = dict(sorted(new_dict.items()))

    
    return new_dict

nomes = {'Ana': 19, 'Bruno': 18, 'João': 19,'Pedro': 18, 'Maria': 17, 'José': 17, 'Carlos': 17}
print(inverte_dicionario(nomes))