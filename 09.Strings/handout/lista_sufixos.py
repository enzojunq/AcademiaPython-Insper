def lista_sufixos(string:str):
    sufixos=[]
    for i in range(len(string)):
        sufixos.append(string[i:])
    return sufixos