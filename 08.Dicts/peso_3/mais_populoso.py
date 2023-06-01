def mais_populoso(pais):
    dict_populacoes={}
    for estados,cidades in pais.items():
        for populacoes,quantidade in cidades.items():
            if estados not in dict_populacoes:
                dict_populacoes[estados]=quantidade
            else:
                dict_populacoes[estados]+=quantidade
    return max(dict_populacoes, key=dict_populacoes.get)





brasil={'São Paulo': {'São Paulo': 1, 'Campinas': 1}, 'Minas Gerais': {'Belo Horizonte': 2, 'Uberlândia': 2}}
print(mais_populoso(brasil))