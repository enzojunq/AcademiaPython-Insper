def agrupa_por_nacionalidade(atletas):
    nacionalidades={}
    for atleta, info in atletas.items():
        nacionalidade=info['nacionalidade']
        if nacionalidade not in nacionalidades:
            nacionalidades[nacionalidade]=[atleta]
        else:
            nacionalidades[nacionalidade].append(atleta)

    return nacionalidades

atletas = {
    "Mathieu BILODEAU": {
        "idade": 37,
        "nacionalidade": "Canadá",
        "modalidade": "Atletismo",
    },
    "Gabriela BITOLO": {
        "idade": 22,
        "nacionalidade": "Brasil",
        "modalidade": "Handebol",
    },
    "Jerome BLAKE": {
        "idade": 25,
        "nacionalidade": "Canadá",
        "modalidade": "Atletismo",
    },
    "Felipe BORGES": {
        "idade": 36,
        "nacionalidade": "Brasil",
        "modalidade": "Handebol",
    },
    "Gabriela BRAGA GUIMARAES": {
        "idade": 27,
        "nacionalidade": "Brasil",
        "modalidade": "Vôlei",
    },
}

print(agrupa_por_nacionalidade(atletas))
