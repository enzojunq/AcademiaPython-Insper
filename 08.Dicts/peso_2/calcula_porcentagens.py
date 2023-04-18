def calcula_porcentagens(resultados):
    porcentagens={}
    total=0
    for resultado in resultados:
        total+=resultados[resultado]
    
    for resultado in resultados:
        porcentagens[resultado]=resultados[resultado]*100/total
    

    return porcentagens


resultados={
    'Erro de indentação': 493,
    'Erro de parênteses': 1102,
    'Variável inexistente': 405,
}
print(calcula_porcentagens(resultados))