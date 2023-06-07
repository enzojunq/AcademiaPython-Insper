def separa_por_inicial(salas):
    estudantes={}
    for sala, alunos in salas.items():
        for aluno in alunos:
            if aluno[0] not in estudantes:
                estudantes[aluno[0]]=[aluno]
            else:
                estudantes[aluno[0]].append(aluno)
    return estudantes




salas = {
    "Sala 1": ["Américo", "Yuri"],
    "Sala 2": ["Marcos"],
    "Sala 3": ["Enzo", "Olívia"],
    "Sala 4": ["Pedro", "Paulo", "Edson"],
}

print(separa_por_inicial(salas))