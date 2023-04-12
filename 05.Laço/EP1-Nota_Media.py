def nota_quizzes(quiz1,quiz2,quiz3,quiz4,quiz5):
    menor=0
    if quiz1<0 or quiz2<0 or quiz3<0 or quiz4<0 or quiz5<0:
        return 0
    elif quiz1>10 or quiz2>10 or quiz3>10 or quiz4>10 or quiz5>10:
        return 0
    else:
        menor=min(quiz1,quiz2,quiz3,quiz4,quiz5)
        media=(quiz1+quiz2+quiz3+quiz4+quiz5-menor)/4
        
        return media
def nota_final(media_quiz,nota_AI,nota_AF,nota_EP1,nota_EP2,nota_PF):
    if media_quiz<0 or media_quiz>10 or nota_AI<0 or nota_AI>10 or nota_AF<0 or nota_AF>10 or nota_EP1<0 or nota_EP1>10 or nota_EP2<0 or nota_EP2>10 or nota_PF<0 or nota_PF>10:
        return 0
    else:
        NI=0.4*nota_AI+0.5*nota_AF+0.1*media_quiz
        NG=0.1*nota_EP1+0.2*nota_EP2+0.7*nota_PF



        if NI>=5 and NG>=5:
            NF=(NI+NG)/2
            return NF
        elif NI<5 or NG<5:
            NF=min(NI,NG)
            return NF
        else:
            return 0
        

notas=[]
total=0
aprovados=0
reprovados=0
adicionar_notas = input("Deseja adicionar notas? ")
while adicionar_notas!='não':
    nota_q1 = float(input("Digite a nota do primeiro quiz: "))
    nota_q2 = float(input("Digite a nota do segundo quiz: "))
    nota_q3 = float(input("Digite a nota do terceiro quiz: "))
    nota_q4 = float(input("Digite a nota do quarto quiz: "))
    nota_q5 = float(input("Digite a nota do quinto quiz: "))
    nota_AI = float(input("Digite a nota da avalição intermediária: "))
    nota_AF = float(input("Digite a nota da avalição final: "))
    nota_EP1 = float(input("Digite a nota do EP1: "))
    nota_EP2 = float(input("Digite a nota do EP2: "))
    nota_PF = float(input("Digite a nota da projeto final: "))
    media_quiz = nota_quizzes(nota_q1,nota_q2,nota_q3,nota_q4,nota_q5)
    final=nota_final(media_quiz,nota_AI,nota_AF,nota_EP1,nota_EP2,nota_PF)
    print(f'Nota final do aluno: {final:.2f}')
    notas.append(final)
    if final>6:
        aprovados=aprovados+1
    else:
        reprovados=reprovados+1
    total=total+1
    adicionar_notas = input("Deseja adicionar notas? ")

if len(notas)>0:
    media_sala=sum(notas)/len(notas)
    print(f'Média da sala: {media_sala:.2f}')

    print(f'Aprovados: {aprovados*100/total:.2f}%')
    print(f'Reprovados: {reprovados*100/total:.2f}%')
else:
    print(f'Média da sala: 0.00%')
    print(f'Aprovados: 0.00%')
    print(f'Reprovados: 0.00%')
