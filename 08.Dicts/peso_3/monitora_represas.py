def monitora_represas(estado_inicial:dict,variacoes:dict):
    represas={}
    represas_saldo={}
    represas_situacao={}
    for nome, dias in variacoes.items():
        for dia, valor in dias.items():
            if nome not in represas_saldo:
                represas_saldo[nome]=valor[0]-valor[1]
            else:
                represas_saldo[nome]+=valor[0]-valor[1]
    
    for nome, dados in estado_inicial.items():
        atual = dados['capacidade'] * dados['volume'] / 100
        if nome not in represas:
            represas[nome]=(atual+represas_saldo[nome])/dados['capacidade'] *100
        else:
            represas[nome]+=(atual+represas_saldo[nome])/dados['capacidade']*100

    for represa,valor in represas.items():
        if valor < 20:
            if 'emergencia' not in represas_situacao:
                represas_situacao['emergencia']=[represa]
            else:
                represas_situacao['emergencia'].append(represa)
        elif valor < 50:
            if 'critico' not in represas_situacao:
                represas_situacao['critico']=[represa]
            else:
                represas_situacao['critico'].append(represa)
        elif valor < 70:
            if 'atencao' not in represas_situacao:
                represas_situacao['atencao']=[represa]
            else:
                represas_situacao['atencao'].append(represa)
        elif valor <= 100:
            if 'normal' not in represas_situacao:
                represas_situacao['normal']=[represa]
            else:
                represas_situacao['normal'].append(represa)
        else:
            if 'escoar' not in represas_situacao:
                represas_situacao['escoar']=[represa]
            else:
                represas_situacao['escoar'].append(represa)

    
    return represas_situacao


    


estado_inicial = {
    'cantareira': {
        'capacidade': 982000, #em litros
        'volume': 25 #em porcentagem
    },
    'guarapiranga': {
        'capacidade': 171000,
        'volume': 95
    },
    'alto tiete': {
        'capacidade': 540000,
        'volume': 55
    }
}
variacoes = {
    'cantareira': {
        '01': [5000,30000], # dia: volume de prcipitacao, consumo
        '02': [10000,35000],
        '03': [0,29000],
        '04': [31000,28000],
        '05': [0,29000]
    },
    'guarapiranga': {
        '01': [6000,10000],
        '02': [38000,12000],
        '03': [35000,14000],
        '04': [0,13000],
        '05': [15000,12000]
    },
    'alto tiete': {
        '01': [18000,30000],
        '02': [15000,25000],
        '03': [17700,24000],
        '04': [41000,28000],
        '05': [13000,24000]
    }
}
print(monitora_represas(estado_inicial,variacoes))