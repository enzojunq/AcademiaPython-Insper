def mais_lancamentos(series,ano):
    plataformas={}
    plats=[]
    
    for serie in series:
        if serie['ano_estreia']==ano:
            if serie['plataforma'] not in plataformas:
                plataformas[serie['plataforma']]=1
            else:
                plataformas[serie['plataforma']]+=1

    if plataformas=={}:
        return []

    resultado=max(plataformas.values())
    for plataforma,valor in plataformas.items():
        if valor == resultado:
            plats.append(plataforma)


    return plats




series = [
    {"plataforma": "Showtime", "titulo": "The Man Who Fell to Earth", "ano_estreia": 2022},
    {"plataforma": "Prime Video", "titulo": "Paper Girls", "ano_estreia": 2022},
    {"plataforma": "Netflix", "titulo": "Altered Carbon", "ano_estreia": 2018},
    {"plataforma": "Paramount", "titulo": "Star Trek: Strange New Worlds", "ano_estreia": 2022},
    {"plataforma": "Paramount", "titulo": "Star Trek: Voyager", "ano_estreia": 1995},
    {"plataforma": "Paramount", "titulo": "The Man Who Fell to Earth", "ano_estreia": 2022},
]

ano = 2022
resultado = mais_lancamentos(series, ano)
print(resultado)