def calcula_estado(lista):
    media_quizzes=[]
    notas=[]
    output=[]
    for aluno in lista:
        menor=min(aluno[1])
        aluno[1].remove(menor)
        media_quizzes.append(sum(aluno[1])/len(aluno[1]))
    #return media_quizzes
    for i in range(len(lista)):
        notas.append(0.1*media_quizzes[i]+lista[i][2][0]*0.4+lista[i][2][1]*0.5)
        if notas[i]>=5:
            output.append([lista[i][0],'A'])
        else:
            output.append([lista[i][0],'R'])
    return output



        
    
        
            
            
# print(calcula_estado([
#     ['Maria', [5.0, 10.0, 0.0, 10.0, 10.0], [6.7, 8.0]],
#     ['Joao', [0.0, 10.0, 10.0, 10.0, 0.0], [6.7, 2.0]],
#     ['Joana', [10.0, 0.0, 10.0, 0.0, 10.0], [6.7, 8.0]]
# ]))
print(calcula_estado([['Yuri', [10.0, 10.0, 10.0, 10.0, 10.0], [0, 8.0]], ['Zé', [0.0, 10.0, 10.0, 10.0, 0.0], [8.7, 6.0]]]))




# formato: [ [Nome do aluno, [notas dos quizzes], [AI, AF]] ]