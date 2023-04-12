def calcula_troco(valor,dinheiro,notas):
    troco=[]
    output=[]
    i=0
    troco1=abs(dinheiro-valor)
    while i < len(notas):
        if notas[i]<=troco1:
            troco.append(notas[i])
            troco1-=notas[i]
            i=0
        else:
            i+=1
    troco2=set(troco)
    troco2=sorted(troco2)
    for nota in troco2:
        qtd = troco.count(nota)
        if nota>1:
            output.append(f"{qtd} nota(s) de R$ {nota}")
        else:
            output.append(f"{qtd} moeda(s) de R$ {nota}")

    output.reverse()
    return output

notas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]
print(calcula_troco(2.25,1000,notas))