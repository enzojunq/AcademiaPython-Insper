def calcula_overbooking(capacidade,passagens_vendidas):
    overbooked=0
    if len(passagens_vendidas)==0:
        return 0
    else:
        for i in passagens_vendidas:
            if i > capacidade:
                overbooked+=i-capacidade
    return overbooked
print(calcula_overbooking(72, [0, 70,73]))