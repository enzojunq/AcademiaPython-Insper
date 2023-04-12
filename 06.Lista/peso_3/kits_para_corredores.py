def organiza_filas(lista):
    fila1=[]
    fila2=[]
    fila3=[]
    fila4=[]

    for pessoa in lista:
        if pessoa[1]<=20:
            fila1.append(pessoa[0])
        elif pessoa[1]<=40:
            fila2.append(pessoa[0])
        elif pessoa[1]<=60:
            fila3.append(pessoa[0])
        else:
            fila4.append(pessoa[0])
    return [fila1,fila2,fila3,fila4]

print(organiza_filas([
	['João',20],['Maria',18],['Mario',35],['Dario',43],
	['Joana',60],['Lucas',27],['Alice',56],['Sofia',32],
	['Bruno',19],['Melissa',61],['Frida',27],['Felipe',30]
]))