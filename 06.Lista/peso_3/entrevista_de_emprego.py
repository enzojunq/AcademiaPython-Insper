def seleciona_candidatos(candidatos,criterios):
    if candidatos == [] or criterios == []:
        return []
    candidatos_selecionados = []
    for candidato in candidatos:
        if len(candidato[2]) != 3:
            continue
        if candidato[2][0] >= criterios[0] and candidato[2][1] >= criterios[1] and candidato[2][2] >= criterios[2]:
            candidatos_selecionados.append(candidato[:2])     
    return candidatos_selecionados

print(seleciona_candidatos([
    ['Maria S.', '456780-9', [3.2, 5.5, 8.0]],
    ['Zeca AD.', '123423-5', [9.5, 5.5, 8.0]],
    ['Vitor B.', '987621-5', [9.0, 2.0, 8.0]],
    ['Ellen R.', '404040-1', [9.5, 9.0, 6.0]]
],[8, 5, 7.5]))
