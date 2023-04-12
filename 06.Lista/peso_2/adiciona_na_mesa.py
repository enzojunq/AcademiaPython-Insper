def adiciona_na_mesa(peca,mesa):
    if len(mesa)==0:
        return [peca]
    inicio_mesa=mesa[0][0]
    final_mesa=mesa[-1][-1]
    #print(inicio_mesa,final_mesa)
    if peca[1]==inicio_mesa:
        mesa.insert(0,peca)
    elif peca[0]==inicio_mesa:
        peca.reverse()
        mesa.insert(0,peca)
    elif peca[1]==final_mesa:
        peca.reverse()
        mesa.append(peca)
    elif peca[0]==final_mesa:
        mesa.append(peca)
    return mesa

    #print(mesa)
print(adiciona_na_mesa([6,6],[]))
