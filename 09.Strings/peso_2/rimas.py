def classifica_rima(palavra1, palavra2, palavra3, palavra4):
    if palavra1 == palavra2 and palavra2 == palavra3 and palavra3 == palavra4:
        return("outra")
    elif palavra1 == palavra3 and palavra2 == palavra4:
        return("alternada")
    elif palavra1 == palavra4 and palavra2 == palavra3:
        return("interpolada")
    elif palavra1 == palavra2 and palavra3 == palavra4:
        return("emparelhada")
    else:
        return("outra")
    
    
print(classifica_rima("ada", "ada", "ada", "ada"))