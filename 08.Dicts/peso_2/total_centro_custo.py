def total_centro_custo(gastos):
    gastos_totais={}
    for pessoa,x in gastos.items():
        if x['centro de custo'] not in gastos_totais:
            gastos_totais[x['centro de custo']]=x['valor']
        else:
            gastos_totais[x['centro de custo']]+=x['valor']
    return gastos_totais