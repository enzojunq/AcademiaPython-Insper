from math import sqrt
def calcula_tempo(atletas:dict):
    resultado={}
    for atleta in atletas:
        aceleracao=atletas[atleta]
        resultado[atleta]=sqrt(100*2/aceleracao)    
    return resultado 

atletas={}
nome=input('Qual é o nome? ')
while nome != 'sair':
    atletas[nome]=float(input('Qual a aceleração? '))
    nome=input('Qual é o nome? ')

tempo_atletas = calcula_tempo(atletas)
menor_tempo=min(tempo_atletas.values())

for nome, tempo in tempo_atletas.items():
    if tempo == menor_tempo:
        print(f'O vencedor é {nome} com tempo de conclusão de {tempo} s')
