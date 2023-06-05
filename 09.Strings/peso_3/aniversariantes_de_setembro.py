def aniversariantes_de_setembro(aniversarios):

    aniversariantes={}
    
    for nome,data in aniversarios.items():
        if data[3:5] == '09':
            aniversariantes[nome]=data

    return aniversariantes


aniversarios = {'Nico Uno': '01/01/1992', 'Horácio P. Genaro': '03/03/1992', 'Ukibe Nokome': '05/05/1992', 'Maurício Melo': '07/09/1992', 'Abigail Oliveira': '09/09/1992'}

print(aniversariantes_de_setembro(aniversarios))