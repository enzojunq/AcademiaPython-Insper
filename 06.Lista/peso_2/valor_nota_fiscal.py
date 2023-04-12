def calcula_total_da_nota(precos, quantidades):
    total=[]
    for i in range(len(precos)):
        total.append(quantidades[i]*precos[i])
    return sum(total)