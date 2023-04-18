def notas_dp(notas):
    lista_alunos_dp=[]
    for alunos in notas:
        if (alunos['PI']+alunos['PF'])/2<5:
            lista_alunos_dp.append(alunos['matricula'])
    return lista_alunos_dp
