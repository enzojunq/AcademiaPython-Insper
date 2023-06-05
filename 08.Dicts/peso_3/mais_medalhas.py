def mais_medalhas(medalhistas: dict) -> str:
    nacionalidades={}
    for medalhista in medalhistas:
        nacionalidade = medalhista['nacionalidade']
        ouro = medalhista['ouro']
        prata = medalhista['prata']
        bronze = medalhista['bronze']
        if nacionalidade not in nacionalidades:
            nacionalidades[nacionalidade]={}
            nacionalidades[nacionalidade]['ouro']=ouro
            nacionalidades[nacionalidade]['prata']=prata
            nacionalidades[nacionalidade]['bronze']=bronze
        else:
            nacionalidades[nacionalidade]['ouro']+=ouro
            nacionalidades[nacionalidade]['prata']+=prata
            nacionalidades[nacionalidade]['bronze']+=bronze

    # se hover empate, desempata por quantidade de pratas
    return max(nacionalidades, key=lambda x: (nacionalidades[x]['ouro'], nacionalidades[x]['prata']))


medalhistas=[{
    'nome': ' Michael Phelps',
    'nacionalidade': 'Norte Americano',
    'ouro': 22, 'prata': 3, 'bronze': 2,
},
{
    'nome': 'Larisa Latynina',
    'nacionalidade': 'Russo',
    'ouro': 10, 'prata': 5, 'bronze': 4,
},
{
    'nome': 'Nikolai Andrianov',
    'nacionalidade': 'Russo',
    'ouro': 10, 'prata': 5, 'bronze': 3,
},
{
    'nome': 'Boris Shakhlin',
    'nacionalidade': 'Russo',
    'ouro': 10, 'prata': 4, 'bronze': 2,
},
{
    'nome': 'Jenny Thompson',
    'nacionalidade': 'Norte Americano',
    'ouro': 8, 'prata': 3, 'bronze': 1,
}]

print(mais_medalhas(medalhistas))