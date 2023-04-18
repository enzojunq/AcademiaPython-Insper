def calcula_media(alunos):
    notas=[]
    for turmas in alunos:
        for aluno in turmas:
            valor=turmas[aluno]
            notas.append(valor)
    return sum(notas)/len(notas)

alunos = [ {"aluno1": 5, "aluno2": 8}, {"aluno3": 5} ]
print(calcula_media(alunos))