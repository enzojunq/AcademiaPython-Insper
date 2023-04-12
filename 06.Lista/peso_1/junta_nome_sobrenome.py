def junta_nome_sobrenome(nomes,sobrenomes):
    nomes_completos=[]
    for i in range(len(nomes)):
        nomes_completos.append(nomes[i]+' '+sobrenomes[i])
    return nomes_completos
        
nomes=['enzo','otto']
sobrenomes=['patelli', 'junqueira']
print(junta_nome_sobrenome(nomes,sobrenomes))
