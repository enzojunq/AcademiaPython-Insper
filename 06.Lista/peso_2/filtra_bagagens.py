def filtra_bagagens(bagagens,altura,largura,profundidade):
    bagagem_excedentes=0
    for bagagem in bagagens:
        if bagagem[0]>altura or bagagem[1]>largura or bagagem[2]>profundidade:
            bagagem_excedentes+=1
    return bagagem_excedentes