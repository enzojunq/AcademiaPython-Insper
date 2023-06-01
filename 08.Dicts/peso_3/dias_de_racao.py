import math
def dias_de_racao(estoques: list,infos: dict):
    if len(estoques)==0:
        return 0

    idade =  infos['idade']
    porte = infos['porte']
    gramas_dia = infos['gramas_dia']

    if idade <=1:
        tamanho = 'filhote'
    elif idade < 8 :
        tamanho = 'adulto'
    else:
        tamanho = 'idoso'

    kg_racao=0

    for estoque,dados in enumerate(estoques):
            
        if dados['porte']==porte and dados['indicado']==tamanho:
            kg_racao+=dados['qtde']
    
    if kg_racao == 0:
        return 0
    
    else:
        return math.floor(kg_racao*1000/gramas_dia)

    




estoque = [
  {
      'marca': 'premier',
      'porte': 'pequeno',
      'indicado': 'adulto',
      'qtde': 8
  },
  {
      'marca': 'royal c.',
      'porte': 'pequeno',
      'indicado': 'filhote',
      'qtde': 2.5
  }
]

animal = {
  'nome': 'totó',
  'idade': 1,
  'porte': 'pequeno',
  'gramas_dia': 200.0
}

print(dias_de_racao(estoque,animal))