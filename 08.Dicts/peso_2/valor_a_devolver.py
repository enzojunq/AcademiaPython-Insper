def valor_a_devolver(prateleira:dict,caixa:dict,compras:list):
    valor_devolver=0
    for produto in compras:
        if caixa[produto[0]][produto[1]] > prateleira[produto[0]][produto[1]]:
            valor_devolver+= abs(caixa[produto[0]][produto[1]]-prateleira[produto[0]][produto[1]])*produto[2]
    return valor_devolver

prateleira={'requeijão': {'Minas': 5, 'Buritis': 6, 'Queijinho': 7}
            , 'sabão': {'Pura Espuma': 10, 'Lavagem Perfeita': 12.5
            , 'Cromo': 15.7}, 'arroz': {'Prato Fundo': 20, 'Tio José': 23
            , 'Cadez': 25}, 'macarrão': {'Sandra': 2, 'Massa Nobre': 4
            , 'Urbano': 5.3}}

caixa     ={'requeijão': {'Minas': 10, 'Buritis': 7, 'Queijinho': 7}
            , 'sabão': {'Pura Espuma': 10.5, 'Lavagem Perfeita': 12.8
            , 'Cromo': 15.8}, 'arroz': {'Prato Fundo': 20, 'Tio José': 23
            , 'Cadez': 23}, 'macarrão': {'Sandra': 2, 'Massa Nobre': 4.5
            , 'Urbano': 5.3}}

compras=[['arroz', 'Cadez', 2],
         ['requeijão', 'Minas', 3],
         ['requeijão', 'Queijinho', 1],
         ['sabão', 'Cromo', 2]]

print(valor_a_devolver(prateleira,caixa,compras))