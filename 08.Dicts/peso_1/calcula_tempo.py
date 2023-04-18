from math import sqrt
def calcula_tempo(atletas):
    resultado={}
    for atleta in atletas:
        aceleracao=atletas[atleta]
        resultado[atleta]=sqrt(100*2/aceleracao)
        
    return resultado 


atletas={'Nico Uno': 10, 'Horácio P. Genaro': 15, 'Ukibe Nokome': 3, 'Maurício Melo': 20, 'Abigail Oliveira': 17}
print(calcula_tempo(atletas))