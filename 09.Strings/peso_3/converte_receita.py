def converte_receita(receita):
    receita_em_ml = {}
    
    for ingrediente, quantidade in receita.items():
        if ingrediente == 'ovos':
            receita_em_ml[ingrediente] = quantidade
            continue
        else:
            if quantidade[2:] == 'xícaras' or quantidade[2:] == 'xícara':
                receita_em_ml.setdefault(ingrediente, 0)
                receita_em_ml[ingrediente] += int(quantidade[0]) * 250
            elif quantidade[2:] == 'colher de sopa' or quantidade[2:] == 'colheres de sopa':
                receita_em_ml.setdefault(ingrediente, 0)
                receita_em_ml[ingrediente] += int(quantidade[0]) * 15
            elif quantidade[2:] == 'colher de chá' or quantidade[2:] == 'colheres de chá':
                receita_em_ml.setdefault(ingrediente, 0)
                receita_em_ml[ingrediente] += int(quantidade[0]) * 5
                
    for ingrediente, valor in receita_em_ml.items():
        if ingrediente == 'ovos':
            continue
        receita_em_ml[ingrediente] = str(valor) + ' ml'
    
    return receita_em_ml




receita = {
  "ovos":"4",
  "açúcar":"2 xícaras",
  "leite":"1 xícara",
  "farinha":"2 xícaras",
  "fermento": "1 colher de sopa",
  "baunilha":"1 colher de chá"
}

print(converte_receita(receita))