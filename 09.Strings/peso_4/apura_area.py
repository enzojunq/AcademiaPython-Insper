def apura_area(votos,candidatos):
    votos_regiao={}
    for secao in votos:
        if secao['area'] not in votos_regiao:
            votos_regiao[secao['area']]={}
        for pessoa,quantidade in secao['candidatos'].items():
            if pessoa == 'nulos':
                if pessoa not in votos_regiao[secao['area']]:
                        votos_regiao[secao['area']][pessoa]=quantidade
                else:
                    votos_regiao[secao['area']][pessoa]+=quantidade
            elif pessoa=='brancos':
                if pessoa not in votos_regiao[secao['area']]:
                        votos_regiao[secao['area']][pessoa]=quantidade
                else:
                    votos_regiao[secao['area']][pessoa]+=quantidade
            else:
                for partido,nomes in candidatos.items():
                    if pessoa in nomes:
                        if partido not in votos_regiao[secao['area']]:
                            votos_regiao[secao['area']][partido]=quantidade
                        else:
                            votos_regiao[secao['area']][partido]+=quantidade

    return votos_regiao


votos_por_secao = [
    {
        'secao': 102,
        'area': 'litoral',
        'candidatos': {
            'ze da esquina': 159,
            'maria do milagre': 231,
            'nulos': 43,
            'brancos': 43
        }
    },
    {
        'secao': 103,
        'area': 'litoral',
        'candidatos': {
            'ze da esquina': 432,
            'maria do milagre': 965,
            'nulos': 63,
            'brancos': 86
        }
    },
    {
        'secao': 431,
        'area': 'capital',
        'candidatos': {
            'tiao da borracharia': 723,
            'maria do milagre': 812,
            'nulos': 3,
            'brancos': 36
        }
    }
]

candidatos_por_partido = {
    'fdb': ['tiao da borracharia', 'frederico ganhador', 'zelia despachante'],
    'ipdt': ['ze da esquina', 'maria do milagre'],
}

print(apura_area(votos_por_secao,candidatos_por_partido))