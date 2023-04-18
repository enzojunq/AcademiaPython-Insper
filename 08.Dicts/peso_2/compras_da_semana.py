def compras_da_semana(receitas,pratos):
    quantidades={}
    for prato in pratos:
        for receita in receitas:
            if receita==prato:
                for ingredientes in receitas[receita]:
                    if ingredientes not in quantidades:
                        quantidades[ingredientes]=receitas[receita][ingredientes]
                    else:
                        quantidades[ingredientes]+=receitas[receita][ingredientes]


    return quantidades


receitas={
    'Bolo de chocolate': {
        'Leite': 0.25,
        'Óleo': 0.25,
        'Ovo': 2.0,
        'Farinha': 0.5,
        'Açúcar': 0.2,
        'Achocolatado': 0.3
    },
    'Bolinho de chuva': {
        'Óleo': 1.0,
        'Leite': 0.3,
        'Ovo': 3.0,
        'Farinha': 0.6,
        'Açúcar': 0.3
    },
    'Mingau': {
        'Açúcar': 0.1,
        'Maizena': 0.1,
        'Leite': 0.25
    }
}
pratos=['Bolinho de chuva', 'Bolo de chocolate', 'Bolinho de chuva']

print(compras_da_semana(receitas,pratos))