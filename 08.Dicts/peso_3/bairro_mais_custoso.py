def total_do_semestre_por_bairro(bairros):
    gastos_p_bairro={}
    for bairro, gastos in bairros.items():
        gasto_total=sum(gastos[6:])
        gastos_p_bairro[bairro]=gasto_total
    return gastos_p_bairro

def bairro_mais_custoso(bairros):
    gastos_p_bairro=total_do_semestre_por_bairro(bairros)
    return max(gastos_p_bairro, key=gastos_p_bairro.get)