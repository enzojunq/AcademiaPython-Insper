
def tem_estoque(pecas:dict,estoque):
    tamanho_estoque=0
    temanho_pecas=0
    for peca_nec , num_pc in pecas.items():
        if peca_nec not in estoque:
            return False
        for peca_est, num_pc_est in estoque.items():
            if peca_nec == peca_est:
                if num_pc>num_pc_est:
                    return False
    return True





pecas={
    'motor': 1,
    'porta esquerda': 1,
    'porta direita': 1,
    'roda': 3,
}

estoque={
    'hélice': 149,
    'porta esquerda': 100,
    'porta direita': 42,
    'roda': 20,
    'turbina': 23,
}
print(tem_estoque(pecas,estoque))