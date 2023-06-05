def agrupa_por_idade(nomes):
    faixa_etaria={}
    faixa_etaria['criança']=[]
    faixa_etaria['adolescente']=[]
    faixa_etaria['adulto']=[]
    faixa_etaria['idoso']=[]
    for nome,idade in nomes.items():
        if idade <=11:        
            faixa_etaria['criança'].append(nome)
        elif idade <= 17:       
            faixa_etaria['adolescente'].append(nome)
        elif idade <= 59:
            faixa_etaria['adulto'].append(nome)
        else:
            faixa_etaria['idoso'].append(nome)
    return faixa_etaria