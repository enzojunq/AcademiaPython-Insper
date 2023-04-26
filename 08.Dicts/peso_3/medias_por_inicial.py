def medias_por_inicial(notas):
    letras={}
    for aluno,nota in notas.items():
        for letra in aluno:
            if letra not in letras:
                letras[letra]=[]
                letras[letra].append(nota)
            else:
                letras[letra].append(nota)
            break
    for letra, notas in letras.items():
        if len(notas) > 1:
            media = sum(notas) / len(notas)
            letras[letra] = media
        else:
            letras[letra] = notas[0]

    return letras

alunos= {
    'Andrew Ayres': 6,
    'Fábio Ikeda': 10,
    'Fábio Kurauchi': 9,
    'Raul Hage': 8
 }
print(medias_por_inicial(alunos))