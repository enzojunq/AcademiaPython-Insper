def pais_campeao(quadro:dict):
    pais_campeao=[]

    ouro={}
    prata={}
    bronze={}
    for paises,medalhas in quadro.items():
        ouro[paises] = medalhas.get('ouro', 0)
        prata[paises]= medalhas.get('prata',0)
        bronze[paises]= medalhas.get('bronze',0)
   
    pais_campeao= sorted (ouro.items(),key=lambda x: (x[1], prata[x[0]], bronze[x[0]]), reverse=True)
    return pais_campeao[0][0]
quadro={
    'China': {
        'ouro': 20,
        'prata': 35,
        'bronze': 40 
    },
    'Canadá': {
        'ouro': 5,
        'prata': 15,
        'bronze': 20
    },
    'Estados Unidos': {
        'ouro': 25,
        'prata': 30,
        'bronze': 40
    },
    'Brasil': {
        'ouro': 10,
        'prata': 10,
        'bronze': 8
    }
}
print(pais_campeao(quadro))